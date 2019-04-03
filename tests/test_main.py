import pytest
from gaql_builder import GAQLBuilder


class TestGAQLBuilder(object):

    def test_operators(self):
        assert len(GAQLBuilder().operators) == 17

        assert '=' in GAQLBuilder().operators
        assert '!=' in GAQLBuilder().operators
        assert '>' in GAQLBuilder().operators
        assert '>=' in GAQLBuilder().operators
        assert '<' in GAQLBuilder().operators
        assert '<=' in GAQLBuilder().operators
        assert 'IN' in GAQLBuilder().operators
        assert 'NOT IN' in GAQLBuilder().operators
        assert 'LIKE' in GAQLBuilder().operators
        assert 'NOT LIKE' in GAQLBuilder().operators
        assert 'CONTAINS ANY' in GAQLBuilder().operators
        assert 'CONTAINS ALL' in GAQLBuilder().operators
        assert 'CONTAINS NONE' in GAQLBuilder().operators
        assert 'IS NULL' in GAQLBuilder().operators
        assert 'IS NOT NULL' in GAQLBuilder().operators
        assert 'DURING' in GAQLBuilder().operators
        assert 'BETWEEN' in GAQLBuilder().operators

    def test_durings(self):
        assert len(GAQLBuilder().durings) == 12

        assert 'LAST_14_DAYS' in GAQLBuilder().durings
        assert 'LAST_30_DAYS' in GAQLBuilder().durings
        assert 'LAST_7_DAYS' in GAQLBuilder().durings
        assert 'LAST_BUSINESS_WEEK' in GAQLBuilder().durings
        assert 'LAST_MONTH' in GAQLBuilder().durings
        assert 'LAST_WEEK_MON_SUN' in GAQLBuilder().durings
        assert 'LAST_WEEK_SUN_SAT' in GAQLBuilder().durings
        assert 'THIS_MONTH' in GAQLBuilder().durings
        assert 'THIS_WEEK_MON_TODAY' in GAQLBuilder().durings
        assert 'THIS_WEEK_SUN_TODAY' in GAQLBuilder().durings
        assert 'TODAY' in GAQLBuilder().durings
        assert 'YESTERDAY' in GAQLBuilder().durings

    def test_orderings(self):
        assert len(GAQLBuilder().orderings) == 2

        assert 'ASC' in GAQLBuilder().orderings
        assert 'DESC' in GAQLBuilder().orderings

    def test_select(self):
        assert GAQLBuilder().select_fields == []
        assert 'campaign.name, campaign.id' in GAQLBuilder().select('campaign.name, campaign.id').select_fields
        assert 'campaign.id' in GAQLBuilder().select(['campaign.name', 'campaign.id']).select_fields
        assert 'campaign.name' in GAQLBuilder().select(['campaign.name', 'campaign.id']).select_fields

        with pytest.raises(ValueError):
            GAQLBuilder().select(123)

    def test_resource_from(self):
        assert GAQLBuilder().resource is None
        assert 'campaign' == GAQLBuilder().resource_from('campaign').resource

        with pytest.raises(ValueError):
            GAQLBuilder().resource_from(123)

        with pytest.raises(ValueError):
            GAQLBuilder().resource_from([123])

    def test_where(self):
        assert GAQLBuilder().where_conditions == []
        assert 'segments.date DURING LAST_30_DAYS' in GAQLBuilder().where('segments.date DURING LAST_30_DAYS').where_conditions
        assert 'segments.date DURING LAST_30_DAYS' in GAQLBuilder().where(['segments.date DURING LAST_30_DAYS']).where_conditions

        with pytest.raises(ValueError):
            GAQLBuilder().where(123)

    def test_add_where(self):
        assert GAQLBuilder().where_conditions == []
        assert 'segments.date DURING LAST_30_DAYS' in GAQLBuilder().add_where(
            field='segments.date',
            operator='DURING',
            value='LAST_30_DAYS'
        ).where_conditions

        with pytest.raises(ValueError):
            GAQLBuilder().add_where(123, 123, 123)

        with pytest.raises(ValueError):
            GAQLBuilder().add_where('segments.date', 'DURING', '123')

    def test_limit(self):
        assert GAQLBuilder().limit_num is None
        assert 2 == GAQLBuilder().limit(2).limit_num

        with pytest.raises(ValueError):
            GAQLBuilder().limit(-1)

        with pytest.raises(ValueError):
            GAQLBuilder().limit(0)

        with pytest.raises(ValueError):
            GAQLBuilder().limit('2')

    def test_order_by(self):
        assert GAQLBuilder().ordering is None
        assert 'campaign.name ASC' == GAQLBuilder().order_by('campaign.name ASC').ordering

        with pytest.raises(ValueError):
            GAQLBuilder().order_by(2)

        with pytest.raises(ValueError):
            GAQLBuilder().order_by([])

    def test_to_string(self):
        builder = GAQLBuilder()
        builder.select(['campaign.id', 'campaign.name'])
        builder.resource_from('campaign')
        builder.where("campaign.resource_name = 'customers/1234567/campaigns/987654'")

        expected = "SELECT \n campaign.id, \n campaign.name \nFROM \n campaign \n"
        expected = expected + "WHERE \n campaign.resource_name = 'customers/1234567/campaigns/987654' \n"

        assert builder.to_string() == expected

        with pytest.raises(ValueError):
            GAQLBuilder().to_string()

    def test_to_string_with_add_where(self):
        builder = GAQLBuilder()
        builder.select(['campaign.id', 'campaign.name'])
        builder.resource_from('campaign')
        builder.add_where(
            field='campaign.resource_name',
            operator='=',
            value="'customers/1234567/campaigns/987654'"
        )

        expected = "SELECT \n campaign.id, \n campaign.name \nFROM \n campaign \n"
        expected = expected + "WHERE \n campaign.resource_name = 'customers/1234567/campaigns/987654' \n"

        assert builder.to_string() == expected

        with pytest.raises(ValueError):
            GAQLBuilder().to_string()
