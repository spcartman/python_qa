Scenario Outline: Add new group
  Given a group list
  Given a group with <name>, <header> and <footer>
  When I add the group to the list
  Then the new group list is equal to the old list with the added group

  Examples:
  | name   | header | footer |
  | bdd_01 | bdd_01 | bdd_01 |
  | bdd_02 | bdd_02 | bdd_02 |


Scenario: Delete a group
  Given a non-empty group list
  Given a random group from the list
  When I delete the group from the list
  Then the new group list is equal to the old list without the deleted group