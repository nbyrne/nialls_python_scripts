def main():
    test_dict = {}
    test_dict['dev1'] = {}

    test_dict['dev1']['CES'] = False
    test_dict['dev1']['BES'] = True
    test_dict['dev2'] = {}
    test_dict['dev2']['CES'] = True
    test_dict['dev2']['BES'] = False

    for key,value in test_dict.items():
        print("key",key,"value", value)

    ('key', 'dev2', 'value', {'BES': False, 'CES': True})
    ('key', 'dev1', 'value', {'BES': True, 'CES': False})

    for key,items in test_dict.items():
        for k,value in items.items():
            print("key",key,"sub-key",k,"value",value)

    ('key', 'dev2', 'sub-key', 'BES', 'value', False)
    ('key', 'dev2', 'sub-key', 'CES', 'value', True)
    ('key', 'dev1', 'sub-key', 'BES', 'value', True)
    ('key', 'dev1', 'sub-key', 'CES', 'value', False)

if __name__ == '__main__':
    main()
