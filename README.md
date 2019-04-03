# GAQL Builder [![Version][version-badge]][version-link] ![MIT License][license-badge]

Generating GAQL (Google Ads Query Language) tool, it is not official library.
Would you like to build GAQL string more easier, you can use this tool, but it would not be validated entirely for all of posible pairing.

Please follow [official documentation](https://developers.google.com/google-ads/api/docs/query/overview).

# Requirements

- Python 2.7.13+ / 3.5.3+
- [pip](https://pip.pypa.io/en/stable/installing/)

# Installation

```bash
  $ pip instal gaql-builder
```

# Usage

If you want to generate the following query string,

```
SELECT
 campaign.id,
 campaign.name
FROM
 campaign
WHERE
 campaign.resource_name = 'customers/1234567/campaigns/987654'
```

you can use functional call to make it out.

```python
    builder = GAQLBuilder()
    builder.select(['campaign.id', 'campaign.name'])
    builder.resource_from('campaign')
    builder.where("campaign.resource_name = 'customers/1234567/campaigns/987654'")
    builder.to_string()
```

also, you can use `add_where` function to add condition.

```python
    builder = GAQLBuilder()
    builder.select(['campaign.id', 'campaign.name'])
    builder.resource_from('campaign')
    builder.add_where(
        field='campaign.resource_name',
        operator='=',
        value="'customers/1234567/campaigns/987654'"
    )
```

### License

[MIT](https://github.com/yo8568/gaql-builder/blob/master/LICENSE)

[version-badge]:   https://img.shields.io/badge/version-1.0.0-brightgreen.svg
[version-link]:    https://pypi.python.org/pypi/gaql-builder
[license-badge]:   https://img.shields.io/github/license/pythonml/douyin_image.svg
