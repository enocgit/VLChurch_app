import datetime
from members.models import Member



# Bithday display function
def check_birthday():
    members = Member.objects.all()
    today = datetime.date.today()
    celebrated_members = []

    for member in members:
        if member.birthday:
                birthday = member.birthday
                if (birthday.month == today.month) and ((birthday.day - today.day >= -2) and (birthday.day - today.day <= 2)):
                        #  print(f'{member.first_name} {member.last_name}  will be celebrated. {birthday}')
                            celebrated_members.append(member)

    return celebrated_members

def get_global_context(request):
    return {
        'current_year': datetime.datetime.now().year,
        'celebrated_members': check_birthday()
    }