student_data = {'id1': {'name': ['Sara'], 'class': ['V'], 'subject_interigation': ['english, math, science']},
                'id2':{'name': ['David'], 'class':['V'], 'subject_interigation': ['english, math, science']},
                'id3':{'name': ['Sara'], 'class':['V'], 'subject_interigation': ['english, math, science']},
                'id4':{'name': ['Sara'], 'class':['V'], 'subject_interigation': ['english, math, science']},
}

result = {}

for key,Value in  student_data.items():
    if Value not in result.values():
        result[key] = Value

print(result)