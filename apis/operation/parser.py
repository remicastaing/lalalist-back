
from flask_restx.reqparse import RequestParser
from flask_restx import inputs

operation_reqparser = RequestParser(bundle_errors=True)


operation_reqparser.add_argument(
    'trinome',
    type=str,
    location='json',
    required=True,
)
operation_reqparser.add_argument(
    'commercial',
    type=str,
    location='json',
    required=True,
)
operation_reqparser.add_argument(
    'date',
    type=inputs.date_from_iso8601,
    location='json',
    required=True,
)
operation_reqparser.add_argument(
    'avant_kms',
    type=float,
    location='json',
    required=True,
)
operation_reqparser.add_argument(
    'avant_peages',
    type=float,
    location='json',
    required=True,
)
operation_reqparser.add_argument(
    'avant_tps',
    type=float,
    location='json',
    required=True,
)
operation_reqparser.add_argument(
    'aller_kms',
    type=float,
    location='json',
    required=True,
)
operation_reqparser.add_argument(
    'aller_peages',
    type=float,
    location='json',
    required=True,
)
operation_reqparser.add_argument(
    'aller_tps',
    type=float,
    location='json',
    required=True,
)
operation_reqparser.add_argument(
    'retour_kms',
    type=float,
    location='json',
    required=True,
)
operation_reqparser.add_argument(
    'retour_peages',
    type=float,
    location='json',
    required=True,
)
operation_reqparser.add_argument(
    'retour_tps',
    type=float,
    location='json',
    required=True,
)
operation_reqparser.add_argument(
    'apres_kms',
    type=float,
    location='json',
    required=True,
)
operation_reqparser.add_argument(
    'apres_peages',
    type=float,
    location='json',
    required=True,
)
operation_reqparser.add_argument(
    'apres_tps',
    type=float,
    location='json',
    required=True,
)
operation_reqparser.add_argument(
    'chargement_tps',
    type=float,
    location='json',
    required=True,
)
operation_reqparser.add_argument(
    'dechargement_tps',
    type=float,
    location='json',
    required=True,
)
operation_reqparser.add_argument(
    'chargement_unite',
    type=float,
    location='json',
    required=True,
)
operation_reqparser.add_argument(
    'chargement_qtt_totale',
    type=float,
    location='json',
    required=True,
)
operation_reqparser.add_argument(
    'chargement_par_tour',
    type=float,
    location='json',
    required=True,
)