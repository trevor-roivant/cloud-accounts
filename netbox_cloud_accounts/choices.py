
from utilities.choices import ChoiceSet


class AccountStatusChoices(ChoiceSet):

    STATUS_RETIRED = 'retired'
    STATUS_ACTIVE = 'active'
    STATUS_DELETED = 'deleted'
    STATUS_TBD = 'to-be-deleted'

    CHOICES = (
        (STATUS_RETIRED, 'Retired', 'orange'),
        (STATUS_ACTIVE, 'Active', 'green'),
        (STATUS_DELETED, 'Deleted', 'cyan'),
        (STATUS_TBD, 'To Be Deleted', 'red'),
    )