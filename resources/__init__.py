

def register_resources(api):
    from .hello import HelloWorld
    from .register import Register
    from .pet import PetSingle
    from .pet_list import PetList
    from .dog_recs import DogRec
    from .people_recs import PeopleRec
    from .pet_finder_access import PFApiAccess
    from .pet_finder_data import PFDataAnimals
    from .pet_finder_org import PFDataOrg

    api.add_resource(HelloWorld, '/hello')
    api.add_resource(Register,'/register-user')
    api.add_resource(PetSingle, '/pet')
    api.add_resource(PetList, '/pet-list')
    api.add_resource(DogRec, '/dog-rec')
    api.add_resource(PeopleRec, '/people-rec')
    api.add_resource(PFApiAccess, '/pf-get-access-token')
    api.add_resource(PFDataAnimals, '/pf-animals')
    api.add_resource(PFDataOrg, '/pf-org')

    