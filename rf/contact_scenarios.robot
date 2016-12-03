*** Settings ***
Library  rf.AddressBook
Library  Collections
Suite Setup  Init Fixtures
Suite Teardown  Destroy Fixtures


*** Test Cases ***
Add contact
    ${old_list}  Get Contact List
    ${contact}  New Contact  rf_first  rf_last  141 Pit Lane Los Angeles CA  814-135-8496  robo@frame.work
    Create Contact  ${contact}
    Append To List  ${old_list}  ${contact}
    ${new_list}  Get Contact List
    Contact Lists Equal  ${old_list}  ${new_list}

Modify contact
    Ensure Contact Exists
    ${old_list}  Get Contact List
    ${contact_to_modify}  Random Entity  ${old_list}
    ${new_data}  New Contact  rf_first_upd  rf_last_upd  5 Wood Road San Jose CA  128-367-0087  upd_robot@frame.work
    Modify Contact  ${contact_to_modify}  ${new_data}
    Remove Values From List  ${old_list}  ${contact_to_modify}
    Append To List  ${old_list}  ${new_data}
    ${new_list}  Get Contact List
    Contact Lists Equal  ${old_list}  ${new_list}

Delete contact
    Ensure Contact Exists
    ${old_list}  Get Contact List
    ${contact_to_delete}  Random Entity  ${old_list}
    Delete Contact  ${contact_to_delete}
    Remove Values From List  ${old_list}  ${contact_to_delete}
    ${new_list}  Get Contact List
    Contact Lists Equal  ${old_list}  ${new_list}