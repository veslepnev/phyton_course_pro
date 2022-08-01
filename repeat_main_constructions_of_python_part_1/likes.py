def likes(people):
    if len(people) == 0:
        return 'Никто не оценил данную запись'
    elif len(people) == 1:
        return f'{people[0]} оценил(а) данную запись'
    elif len(people) == 2:
        return f'{people[0]} и {people[1]} оценили данную запись'
    elif len(people) == 3:
        return f'{people[0]}, {people[1]} и {people[2]} оценили данную запись'
    elif len(people) > 3:
        return f'{people[0]}, {people[1]} и {len(people) - 2} других оценили данную запись'