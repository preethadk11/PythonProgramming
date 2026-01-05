employess=['kelly','Emma']
defaults={'designation':'developer','salary':8000}
'''res=dict.fromkeys(employess,defaults)
print(res)'''
res={emp: defaults.copy() for emp in employess}
print(res)
