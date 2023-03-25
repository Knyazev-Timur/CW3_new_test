
class Operation:

    def __init__(self, id, state, date, amount, currency, card, from_, to, description):

        self.id = id
        self.state = state
        self.date = date
        self.amount = amount
        self.currency = currency
        self.description = description
        self.card = card
        self.from_ = from_
        self.to = to

    # def __repr__(self):
    #     return {
    #         "id": self.id,
    #         "state": self.state,
    #         "date": self.date,
    #         "amount": self.amount,
    #         "currency": self.currency,
    #         "description": self.description,
    #         "card": self.card,
    #         "from": self.from_,
    #         "to": self.to
    #             }

    def get_id(self):
        return self.id

    def get_state(self):
        return self.state

    def get_date(self):
        return self.date

    def get_amount(self):
        return self.amount

    def get_currency(self):
        return self.currency

    def get_description(self):
        return self.description

    def get_card(self):
        return self.card

    def get_from(self):
        if self.from_ is None:
            return None
        else:
            self.from_ = f'{self.from_[0:4]} {self.from_[4:7]}** **** {self.from_[-4:]}'
            return self.from_

    def get_to(self):
        self.to =f'**{self.to[-4:]}'
        return self.to

