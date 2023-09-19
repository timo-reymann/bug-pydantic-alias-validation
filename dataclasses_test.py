import unittest

from dataclass import PaymentInfoModel


class TestDataClass(unittest.TestCase):
    def test_constructor(self):
        obj = PaymentInfoModel(allowedPaymentMethods=["credit_card", "sepa"])
        assert len(obj.allowed_payment_methods) == 2

    def test_parse_from_dict(self):
        obj = PaymentInfoModel.from_dict({
            # allowed_payment_methods is defined as alia for allowedPaymentMethods
            "allowed_payment_methods": [
                "credit_card",
                "sepa"
            ]
        })
        # allowed_payment_methods will be None
        assert len(obj.allowed_payment_methods) == 2
