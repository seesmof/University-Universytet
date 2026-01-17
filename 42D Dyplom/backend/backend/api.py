from ninja import NinjaAPI

api = NinjaAPI()


@api.get("/")
def index(request):
    return {"message": "Jesus Christ is LORD"}
