class GAQLBuilder(object):
    def __init__(self):
        self.select_fields = []
        self.resource = None
        self.where_conditions = []
        self.ordering = None
        self.limit_num = None
        self.result = ''

    @property
    def operators(slef):
        return [
            '=', '!=', '<', '<=', '>=', '>',
            'IN', 'NOT IN', 'LIKE', 'NOT LIKE',
            'CONTAINS ANY', 'CONTAINS ALL', 'CONTAINS NONE',
            'IS NULL', 'IS NOT NULL', 'DURING', 'BETWEEN'
        ]

    @property
    def orderings(self):
        return ['ASC', 'DESC']

    @property
    def durings(slef):
        return [
            'LAST_14_DAYS', 'LAST_30_DAYS', 'LAST_7_DAYS',
            'LAST_BUSINESS_WEEK', 'LAST_MONTH', 'LAST_WEEK_MON_SUN',
            'LAST_WEEK_SUN_SAT', 'THIS_MONTH', 'THIS_WEEK_MON_TODAY',
            'THIS_WEEK_SUN_TODAY', 'TODAY', 'YESTERDAY'
        ]

    def select(self, fields):
        if isinstance(fields, list):
            self.select_fields = fields
        elif isinstance(fields, str):
            self.select_fields = [fields]
        else:
            raise ValueError('Args are invalid, it should be a list or a str.')

        return self

    def resource_from(self, resource):
        if isinstance(resource, str):
            self.resource = resource
        else:
            raise ValueError('Args are invalid, it should be a str.')

        return self

    def where(self, conditions):
        if isinstance(conditions, list):
            self.where_conditions = conditions
        elif isinstance(conditions, str):
            self.where_conditions = [conditions]
        else:
            raise ValueError('Args are invalid, it should be a list or a str.')

        return self

    def add_where(self, field, operator, value, mode='AND'):
        if isinstance(field, str) is False:
            raise ValueError('field is invalid, it should be a str.')

        if isinstance(operator, str) is False or operator not in self.operators:
            raise ValueError('operator is invalid, it should be a str.')

        if isinstance(value, str) is False:
            raise ValueError('value is invalid, it should be a str.')

        if operator == 'DURING':
            if value not in self.durings:
                raise ValueError('value is invalid, it should be included in during options.')

        if len(self.where_conditions):
            self.where_conditions.append('%s %s %s %s' % (mode, field, operator, value))
        else:
            self.where_conditions.append('%s %s %s' % (field, operator, value))

        return self

    def order_by(self, ordering):
        if isinstance(ordering, str):
            self.ordering = ordering
        else:
            raise ValueError('Args are invalid, it should be a str.')

        return self

    def limit(self, limit):
        if isinstance(limit, int) and limit > 0:
            self.limit_num = limit
        else:
            raise ValueError('Args are invalid, it should be a positive int.')

        return self

    def _compile(self):
        if len(self.select_fields) == 0 or self.resource is None:
            raise ValueError('Select and From resource are required.')

        self.result = 'SELECT \n %s \n' % ', \n '.join(self.select_fields)
        self.result = self.result + 'FROM \n %s \n' % self.resource

        if len(self.where_conditions):
            self.result = self.result + 'WHERE \n %s \n' % '\n AND '.join(self.where_conditions)

        if self.ordering:
            self.result = self.result + 'ORDER BY \n %s \n' % self.ordering

        if self.limit_num:
            self.result = self.result + 'LIMIT \n %s' % self.limit_num

        return self

    def to_string(self):
        self._compile()

        return self.result
