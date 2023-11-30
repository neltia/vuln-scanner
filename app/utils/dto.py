from flask_restx import Namespace, fields


class CheckerDto:
    api = Namespace(
        'checker',
        description='Trivy 컨테이너를 사용한 도커 이미지 취약점 진단 API'
    )

    report = api.model('report', {})
