from pyscript import display, document


def result_checker(e):
    document.getElementById('output').innerHTML = ""

    # Grade level sets with student names
    grade7 = {'Taranbir Singh', 'Rafael Magdayao', 'Lucas Flores'}
    grade8 = {'Joseph Co', 'Joel Gonzales', 'Jarence Manacap', 'Jaden Galvez'}
    grade9 = {'Hans Baquiran', 'Franco Maglaqui', 'Chester Roxas'}
    grade10 = {'Amanda Bower','Luis Bacay','Cedric Visorde','Savannah Reyes',}

    # Retrieve and clean up input values
    first_name = document.getElementById('first_name').value.strip()
    last_name = document.getElementById('last_name').value.strip()

    new_member = f'{first_name} {last_name}'.title()
    new_members_set = {new_member}

    all_members = grade7 | grade8 | grade9 | grade10 | new_members_set
    total_members = len(all_members)

    # Format members 
    sorted_members = sorted(all_members)
    members_badges = ''.join(
        [f"<span class='member-badge'>{m}</span>" for m in sorted_members]
    )

    members_list = "<br>".join(sorted(all_members))

    document.getElementById('output').innerHTML = f'All members:<br>  {members_list}'
    display(f'Total members: {total_members}', target='output') 

