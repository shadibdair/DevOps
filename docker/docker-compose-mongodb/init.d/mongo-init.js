db.createUser(
    {
        user: "admin-devops",
        pwd: "password-devops",
        roles: [
            {
                role: "readWrite",
                db: "newdbadmin"
            }
        ]
    }
);

db.createUser(
    {
        user: "core",
        pwd: "password-core",
        roles: [
            {
                role: "readWrite",
                db: "coreDB"
            }
        ]
    }
);


// If need to create admin user
// db.createUser(
//     {
//         user: "admin",
//         pwd: "admin",
//         roles: [
//           { role: "userAdminAnyDatabase", db: "admin" },
//           { role: "readWrite", db: "admin" }
//         ]
//     });