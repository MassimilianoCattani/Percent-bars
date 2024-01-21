# Percent-bars
Calculate shared percentage of each element.

- User select one of the option.
- Each option gets updated: 'n' times gets picked by the user and relative shared percentage.
- Display updated data and relative % bar of each element.

## Structure

Dictionary:

Keys are the available options. Each options has a sub dict holding two key/value pairs:
  - key/value pair to hold the number of time the option has been selected {'n':0}.
  - key/value pair to keep updated the shared percentage{'per':0}.

    
5 functions: 

- main() -> Gets the given dictionary as a argument (It is used for display option and to be passed to the user_sele() function). User inp, validation structure and display are within this function.
  
- user_sele() -> (Args: dictionary, user inp) Catches the user inp (already validated in main()) and finds the matching option via key. Accesses the sub dict and update the 'n' key value: {n:1}. Returns updated 'dict'.
  
- total_inp() -> (Args: updated dictionaty) Catches the total of the selections by identifying the key 'n' in the sub dict of each option and sums up all the values. Returns updated ('int') total.
  
- update_per() -> (Args: updated dict, total_inp()) Calculate the percentage of each option based on its own number of selection ('n') in relation to the total number of selections. Return updated dict ({'per': 20}).

- display() -> (Args: updated dict, total_inp()) Use total_inp() just for display. Picks data from updated dictionary and display selected info in a formatted way.  
