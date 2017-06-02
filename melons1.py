"""Classes for melon orders."""

class AbstractMelonOrder(object):

    def __init__(self, species, qty, country_code=0):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = "domestic"
        self.tax = 0.08

    def get_total(self):
        """Calculate price, including tax."""
        
        if self.species == "Christmas":
            base_price = 5 * 1.5
        else:
            base_price = 5
        
        if (self.order_type == "international" and self.qty < 10):
            total = ((1 + self.tax) * self.qty * base_price) + 3

        else:    
            total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

class GovernmentMelonOrder(AbstractMelonOrder):
    """Government Melon Order."""

    def __init__(self, species, qty):
        """Initialize Government melon order attributes."""
        super(GovernmentMelonOrder, self).__init__(species, qty)
        self.tax = 0
        self.passed_inspection = False

    def mark_inspection(self, passed):
        """Record inspection status."""

        if passed == 'True':
            self.passed_inspection = True



class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        super(InternationalMelonOrder, self).__init__(species, qty)
        self.country_code = country_code
        self.order_type = "international"
        self.tax = 0.17

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

