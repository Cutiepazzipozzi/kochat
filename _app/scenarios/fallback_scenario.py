<<<<<<< HEAD
"""
@auther Hyunwoong
@since {6/21/2020}
@see : https://github.com/gusdnd852
"""
from _app.scenarios.base_scenario import BaseScenario


class FallbackScenario(BaseScenario):

    def __call__(self) -> dict:
        """
        fallback시 (에러 발생시)
        fallback 딕셔너리 리턴

        :return: fallback 딕셔너리
        """

        return {'intent': 'FALLBACK',
                'entity': 'FALLBACK',
                'answer': 'FALLBACK',
                'state': 'FALLBACK'}
=======
"""
@auther Hyunwoong
@since {6/21/2020}
@see : https://github.com/gusdnd852
"""
from _app.scenarios.base_scenario import BaseScenario


class FallbackScenario(BaseScenario):

    def __call__(self) -> dict:
        """
        fallback시 (에러 발생시)
        fallback 딕셔너리 리턴

        :return: fallback 딕셔너리
        """

        return {'intent': 'FALLBACK',
                'entity': 'FALLBACK',
                'answer': 'FALLBACK',
                'state': 'FALLBACK'}
>>>>>>> 998bcd017cd44db5c996455ee9ee1193cb11520e