def show_detils(name,*skills):
    print(f'Hello {name.upper()} Your Skills Is: ')
    for skill in skills:
        print(skill.upper())
show_detils('abood','Html','Js','Python','Msql')