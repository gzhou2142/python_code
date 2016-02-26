test = {
  'name': 'Dictionaries',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> pokemon = {'pikachu': 25, 'dragonair': 148, 'mew': 151}
          >>> pokemon['pikachu']
          cb65f2ff357d7368f6d293aaf0bbd356
          # locked
          >>> len(pokemon)
          74689fcda5421388b764b40ec8de8ccd
          # locked
          >>> pokemon['jolteon'] = 135
          >>> pokemon['ditto'] = 25
          >>> len(pokemon)
          36823867c25d95f8a792b4dde2bf0d63
          # locked
          >>> sorted(list(pokemon.keys())) # Alphabetically sorted list of pokemon's keys
          46a11a9ef598a571fc5e656e76cc6618
          # locked
          >>> 'mewtwo' in pokemon
          ac667055c8e3c84ad7260b0fefa2e007
          # locked
          >>> pokemon['ditto'] = pokemon['jolteon']
          >>> sorted(list(pokemon.keys())) # Alphabetically sorted list of pokemon's keys
          46a11a9ef598a571fc5e656e76cc6618
          # locked
          >>> pokemon['ditto']
          c375daa87e984186b739dee6d6f04f1b
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}