from masonite.routes import Route
from .controllers.UsersController import UsersController

ROUTES = {
    "User Management": [
        Route.get("/dashboard/users/all", UsersController.index).name("Manage Users"),
        Route.get("/dashboard/users/@id/edit", UsersController.edit),
        Route.post("/dashboard/users/@id/update", UsersController.update)
    ]

}