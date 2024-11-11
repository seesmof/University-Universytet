from nicegui import ui

generic_memory__load__memory='74,9%'
generic_memory__data__used_memory='11,9 GB'
generic_memory__data__available_memory='4,0 GB'
tree_data=[
    {'id':'Generic Memory', 'children': [
        {'id':'Load','children':[
            {'id':f'Memory: {generic_memory__load__memory}'}
        ]},
        {'id':'Data','children':[
            {'id':f'Used Memory: {generic_memory__data__used_memory}'},
            {'id':f'Available Memory: {generic_memory__data__available_memory}'},
        ]}
    ]}
]

def update_data():
    global generic_memory__load__memory
    global generic_memory__data__available_memory
    global generic_memory__data__used_memory
    generic_memory__load__memory='77,7%'
    generic_memory__data__used_memory='12,3 GB'
    generic_memory__data__available_memory='3,7 GB'
    global tree_data
    tree_data=[
        {'id':'Generic Memory', 'children': [
            {'id':'Load','children':[
                {'id':f'Memory: {generic_memory__load__memory}'}
            ]},
            {'id':'Data','children':[
                {'id':f'Used Memory: {generic_memory__data__used_memory}'},
                {'id':f'Available Memory: {generic_memory__data__available_memory}'},
            ]}
        ]}
    ]
    t.update()

t=ui.tree(tree_data, label_key='id').expand()
ui.button('Update',on_click=update_data)
t.bind_visibility_from(tree_data)

l=ui.label('ALLELUJAH')
ui.button('AMEN',on_click=lambda: l.text('PRAISE JESUS'))

ui.run()