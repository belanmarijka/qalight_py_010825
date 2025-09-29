from ls_18_petstore import get_pet, post_pet, delete_pet

def test_get():
    _id = 5
    json_r = get_pet(_id)
    assert json_r["id"] == _id
    assert json_r['name'] == 'doggie'

