
const BASE_URL = "http://127.0.0.1:8000";

async function signup() {

    const phone =
        document.getElementById(
            "phone"
        ).value;

    const password =
        document.getElementById(
            "password"
        ).value;



    const response =
        await fetch(
            `${BASE_URL}/auth/signup`,
            {

                method:"POST",

                headers:{
                    "Content-Type":
                    "application/json"
                },

                body:JSON.stringify({

                    phone:phone,
                    password:password

                })

            }
        );



    const data =
        await response.json();


    console.log(data);


    if(!response.ok){

        alert(
            data.detail
        );

        return;
    }


    alert(
        data.msg
    );


    window.location.href=
    "/auth/login";

}


async function login() {

    const phone =
        document.getElementById("phone").value;

    const password =
        document.getElementById("password").value;


    const response = await fetch(
        `${BASE_URL}/auth/login`,
        {

            method: "POST",

            headers: {
                "Content-Type":
                    "application/json"
            },

            body: JSON.stringify({

                phone: phone,
                password: password

            })

        }
    );


    const data = await response.json();
    if (!data.access_token) {

    alert(data.msg);

    return;

}

    localStorage.setItem(
        "token",
        data.access_token
    );


    profile();
}



async function profile() {


    const token =
        localStorage.getItem("token");


    const response = await fetch(
        `${BASE_URL}/auth/profile`,
        {

            method: "GET",

            headers: {

                Authorization:
                    `Bearer ${token}`

            }

        }
    );


    const data = await response.json();

    console.log(data);
if(response.ok){
    window.location.href="/base_dashboard/dashboard"}
}
function logout() {


    localStorage.removeItem(
        "token"
    );


    window.location.href =
        "/auth/login";

}

async function customer() {
 
        const name =
        document.getElementById("name").value;
    
        const phone =
        document.getElementById("phone").value;

       const amount =
        document.getElementById("amount").value;
       
       const mode =
         document.getElementById("mode").value;


const token =
localStorage.getItem(
"token"
);



const response =
await fetch(
`${BASE_URL}/base_dashboard/customer`,
{

method:"POST",

headers:{

"Content-Type":
"application/json",

Authorization:
`Bearer ${token}`

},


body:JSON.stringify({

name:name,

phone:phone,

amount:amount,
mode:mode
})

}
);



const data =
await response.json();

alert(
JSON.stringify(data)
);

}

async function searchCustomer(){

const name=
document.getElementById(
"search"
).value;


const date=
document.getElementById(
"date"
).value;


const response=
await fetch(

`${BASE_URL}/base_dashboard/search?name=${name}&date=${date}`

);


const data=
await response.json();

alert(
JSON.stringify(data)
);
const result=
document.getElementById(
"result"
);


result.innerHTML="";


data.forEach(customer=>{

result.innerHTML += `

<p>

${customer.name}
-
${customer.phone}
-
₹${customer.amount}

</p>

`;

});

}