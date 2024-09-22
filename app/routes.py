from flask import Blueprint, render_template, request, jsonify
from .models import Avaliacao, db

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            nome = request.form.get('nome')
            tipo = request.form.get('tipo')
            cidade = request.form.get('cidade')
            avaliacao = request.form.get('avaliacao')
            comentario = request.form.get('comentario')
            palavras_chave = request.form.get('palavras-chave')
            latitude = float(request.form.get('latitude'))
            longitude = float(request.form.get('longitude'))

            nova_avaliacao = Avaliacao(
                nome=nome,
                tipo=tipo,
                cidade=cidade,
                comentario=comentario,
                palavras_chave=palavras_chave,
                latitude=latitude,
                longitude=longitude,
                avaliacao=avaliacao
            )

            db.session.add(nova_avaliacao)
            db.session.commit()

            return jsonify({"success": True, "message": "Avaliação adicionada com sucesso!"})
        except Exception as e:
            print(f"Erro ao processar solicitação: {str(e)}")
            db.session.rollback()
            return jsonify({"success": False, "message": str(e)}), 400

    return render_template('index.html')

@main.route('/avaliacoes', methods=['GET'])
def get_avaliacoes():
    avaliacoes = Avaliacao.query.all()
    return jsonify([{
        'id': a.id,
        'nome': a.nome,
        'tipo': a.tipo,
        'cidade': a.cidade,
        'avaliacao': a.avaliacao,
        'comentario': a.comentario,
        'palavras_chave': a.palavras_chave,
        'latitude': a.latitude,
        'longitude': a.longitude
    } for a in avaliacoes])