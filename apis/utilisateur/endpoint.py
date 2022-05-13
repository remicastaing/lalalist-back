from http import HTTPStatus
from flask_restx import Namespace, Resource, fields

from apis.utilisateur.dao import UtilisateurDAO
from apis.utilisateur.parser import create_utilisateur_reqparser

ns = Namespace('utilisateurs', description='opérations relatives aux utilisateurs')

utilisateur = ns.model('Utilisateur', {
    'id': fields.String(required=True, description='Reponse'),
    'prenom': fields.String(required=True, description='Reponse'),
    'nom': fields.String(required=True, description='Reponse'),
    'email': fields.String(required=True, description='Reponse'),
})

DAO = UtilisateurDAO()


@ns.route('/')
class UtilisateursList(Resource):
    @ns.doc('list_utilisateurs')
    @ns.marshal_list_with(utilisateur)
    def get(self):
        """
        Retourne l'ensemble des utilisateurs
        """
        return DAO.getAll()

    @ns.doc('create_utilisateurs')
    @ns.marshal_with(utilisateur)
    @ns.expect(create_utilisateur_reqparser)
    @ns.response(int(HTTPStatus.CREATED), "Un utilisateur a été créé.")
    @ns.response(int(HTTPStatus.FORBIDDEN), "Vous n'avez pas accès.")
    @ns.response(int(HTTPStatus.CONFLICT), "L'utilisateur existe déjà.")
    def post(self):
        """ Crée un utilisateur"""

        utilisateur_dict = create_utilisateur_reqparser.parse_args()
        prenom = utilisateur_dict['prenom']
        nom = utilisateur_dict['nom']
        email = utilisateur_dict['email']
        return DAO.create_utilisateur(prenom, nom, email)


@ns.route('/<string:id>')
@ns.response(404, "L'uilisateur n'a pas été trouvé")
@ns.param('id', "L'uuid de l'utilisateur")
class Utilisateur(Resource):
    '''Retourne un seul utilisateur'''
    @ns.doc('get_utilisateur')
    @ns.marshal_with(utilisateur)
    def get(self, id):
        '''Retourne un utilisateur'''
        return DAO.get(id)

    # @ns.doc('delete_todo')
    # @ns.response(204, 'Todo deleted')
    # def delete(self, id):
    #     '''Delete a task given its identifier'''
    #     DAO.delete(id)
    #     return '', 204

    # @ns.expect(todo)
    # @ns.marshal_with(todo)
    # def put(self, id):
    #     '''Update a task given its identifier'''
    #     return DAO.update(id, api.payload)