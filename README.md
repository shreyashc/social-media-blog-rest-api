# Social Media/ Blog REST API

## live

[https://hcblogapi.herokuapp.com/](https://hcblogapi.herokuapp.com/)

## (Django,drf,PostgreSQL)

Fully fledged rest api for social-media/blog
using **Django** and **Django-rest-framework** and
**PostgreSQL**(ORM).

## features:

-   create,read,update,delete Blogs
-   user signup/login/password-update
-   comments
-   likes
-   Token Authentication
-   custom Admin pannel (/admin)
-   search filters
-   .....

### TODO:

-   replace defatut tokens with JWTs

## setup

-   db configuration

default(sqlLite)

```python
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

postgres

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dbname',
        'USER': 'dbuser',
        'PASSWORD': 'dbpassword',
        'HOST': 'dbhost',
        'PORT': '5432',
    }
}
```

install

```python
    pip install -r requirements.txt
    python manage.py migrate
    python manage.py runserver
```

CORS is disabled by default

## ROUTES :

## signup

-   /signup/
    -   method : POST

```javascript
body
{
    "username": REQUIRED
    "email":  REQUIRED
    "password": REQUIRED
    "bio": OPTIONAL
}

//axios

//request
axios.post('BASE_URL/signup/',{
	username:'shreyas',
	email:'shreyas@gmail.com',
	password:'1@345*hc'
})
.then((res)=>{
	console.log(res.data)
}).catch(err=>{
	console.log(err.response.data)
})


//response
{
  username: 'shreyas',
  email: 'shreyas@gmail.com',
  token: '15892a7a87be9892f42db64b9ed76535c59a0b26'
}
//errors
    {
        username: [ 'This field is required.' ],
        email: [ 'This field is required.' ],
        password: [ 'This field is required.' ]
    },

    {
        username: [ 'username is already taken' ],
        email: [ 'email is already registred' ],
        password: [ 'Ensure this field has at least 8 characters.' ]
    }

```

---

## login

-   /login/
    -   method : POST

```javascript
//axios

//request
axios
    .post("BASE_URL/login/", {
        username: "shreyas",
        password: "1@345*hc",
    })
    .then((res) => {
        console.log(res.data);
    })
    .catch((err) => {
        console.log(err.response.data);
    });

//response
{
  id: 4,
  username: 'shreyas',
  email: 'shreyas@gmail.com',
  auth_token: 'e66628c5bb784e4b0c3366eecac938e18431ccbd'
}

//errors
{
  username: [ 'This field is required.' ],
  password: [ 'This field is required.' ]
},
{
    [ 'Invalid username/password' ]
}
```

## update profile

-   /update-profile/
    -   method : PUT / PATCH
    -   Auth : REQUIRED

```javascript
//axios

//request
axios
    .patch(
        "BASE_URL/update-profile/",
        {
            email: "newEmail@gmail.com",
            bio: "bio update",
        },
        {
            headers: {
                //Token which you will get after login/signup
                Authorization: "Token e66628c5bb784e4b0c3366eecac938e18431ccbd",
            },
        }
    )
    .then((res) => {
        console.log(res.data);
    })
    .catch((err) => {
        console.log(err.response.data);
    });

//reponse
{
  message: 'Profile updated successfully',
  data: [ 'email:newEmail@gmail.com', 'bio:bio update' ]
}

//errors
{
    //400
    email: [ 'Enter a valid email address.' ]
},
{
    //401
    detail: 'Authentication credentials were not provided.'
}
```

## change password

-   /change-password/
    -   method : PUT / PATCH
    -   Auth : REQUIRED

```javascript
//axios

//request
axios
    .patch(
        "BASE_URL/change-password/",
        {
            old_password: "1@345*hc",
            password1: "qwerty123",
            password2: "qwerty123",
        },
        {
            headers: {
                 //Token which you will get after login/signup
                Authorization: "Token e66628c5bb784e4b0c3366eecac938e18431ccbd",
            },
        }
    )
    .then((res) => {
        console.log(res.data);
    })
    .catch((err) => {
        console.log(err.response.data);
    });

//response
{
  status: 'success',
  code: 200,
  message: 'Password updated successfully',
  data: []
  //Token remains the same.
}

//errors
{
  old_password: [ 'This field is required.' ],
  password1: [ 'This field is required.' ],
  password2: [ 'This field is required.' ]
},
{
  password1: [ 'Ensure this field has at least 8 characters.' ],
  password2: [ 'Ensure this field has at least 8 characters.' ]
},
{
    old_password: [ 'incorrect password.' ]
}

```

---

# blogs

### Get All Blogs

-   /blogs/
    -   method : GET

```javascript

//fetchApi
//request
fetch('BASE_URL/blogs/', {
  method: 'GET',
})
.then(response => response.json())
.then(data => console.log(data))
.catch(err=>console.log(err))


//axios
//request
axios
    .get("BASE_URL/blogs/")
    .then((res) => {
        console.log(res.data);
    })
    .catch((err) => {
        console.log(err.response.data);
    });
//resopnse
{
  count: 6,
  next: null,
  previous: null,
  results: [
    {
      id: 6,
      author: {
                "id": 1,
                "username": "shreyashc"
            },
      title: 'last blog2',
      category: 'pythonlkn',
      description: 'sdafdsfl;',
      content: 'sfdsafdskm',
      thumbnail: 'BASE_URL/media/images/blog_thumbnails/Untitled-1.psd',
      created_at: '2020-09-24T05:38:33.257468Z',
      no_of_likes: 0,
      no_of_comments: 0,
      comment: [],
      likes: []
    },
    {
      id: 5,
      author: {
                "id": 1,
                "username": "shreyashc"
            },
      title: 'last blog',
      category: 'python',
      description: 'sdafdsf',
      content: 'sfdsafds',
      thumbnail: 'BASE_URL/media/images/blog_thumbnails/Photo_20200607_153944.jpg',
      created_at: '2020-09-24T05:38:05.107503Z',
      no_of_likes: 0,
      no_of_comments: 0,
      comment: [],
      likes: []
    },
    ......
    ......
    ......
```

## get a single blog

-   /blogs/:id (Int)
    -   method : GET

```javascript

//fetchApi
//request
fetch('BASE_URL/blogs/2', {
  method: 'GET',
})
.then(response => response.json())
.then(data => console.log(data))
.catch(err=>console.log(err))


//axios
//request
axios
    .get("BASE_URL/blogs/2")
    .then((res) => {
        console.log(res.data);
    })
    .catch((err) => {
        console.log(err.response.data);
    });

//response
{
  id: 2,
  author: {
       id: 2, username: 'manu'
       },
  title: 'Android',
  category: 'categeory test',
  description: 'this is a simple description',
  content: "this is content.",
  thumbnail: null,
  created_at: '2020-09-22T06:15:40.646519Z',
  no_of_likes: 2,
  no_of_comments: 1,
  comment: [
            {
            "id": 3,
            "text": "hello",
            "commented_by": {
                "id": 1,
                "username": "shreyashc"
            }
        }
            ],
  likes: [
           {
            "id": 2,
            "liked_by": {
                "id": 1,
                "username": "shreyashc"
            }
        },
        {
            "id": 3,
            "liked_by": {
                "id": 2,
                "username": "manu"
            }
        }
        ]
}
```

## create a blog

-   /blogs/
    -   method : POST
    -   Auth : REQUIRED

```javascript

//axios
//request
axios
    .post(
        "BASE_URL/blogs/",
        {
            title: "This is new blog.",
            description: "this is description",
            content: "content goes here",
        },
        {
            headers: {
                 //Token which you will get after login/signup
                Authorization: "Token e66628c5bb784e4b0c3366eecac938e18431ccbd",
            },
        }
    )
    .then((res) => {
        console.log(res.data);
    })
    .catch((err) => {
        console.log(err.response.data);
    });

//response
{
  id: 7,
  author: { id: 4, username: 'shreyas' },
  title: 'This is new blog.',
  category: null,
  description: 'this is description',
  content: 'content goes here',
  thumbnail: null,
  created_at: '2020-09-26T06:05:45.786195Z',
  no_of_likes: 0,
  no_of_comments: 0,
  comment: [],
  likes: []
}

//errors
{
  title: [ 'This field is required.' ],
  description: [ 'This field is required.' ]
},
{
    detail: 'Authentication credentials were not provided.'
 }
```

## edit a blog

-   /blogs/:blog-id (Int)/
    -   method : PUT/ PATCH
    -   Auth : REQUIRED

```javascript
//axios

//request
axios
    .patch(
        "BASE_URL/blogs/7/",
        {
            title: "This is new blod has been editd.",
            category: "fun",
        },
        {
            headers: {
                 //Token which you will get after login/signup
                Authorization: "Token e66628c5bb784e4b0c3366eecac938e18431ccbd",
            },
        }
    )
    .then((res) => {
        console.log(res.data);
    })
    .catch((err) => {
        console.log(err.response.data);
    });

//response
{
  id: 7,
  author: { id: 4, username: 'shreyas' },
  title: 'This is new blod has been editd.',
  category: 'fun',
  description: 'this is description',
  content: 'content goes here',
  thumbnail: null,
  created_at: '2020-09-26T06:05:45.786195Z',
  no_of_likes: 0,
  no_of_comments: 0,
  comment: [],
  likes: []
}

//errors
{
    detail: 'Authentication credentials were not provided.'
 }
```

## delete a blog

-   /blogs/:blog-id (Int)/
    -   method : DELETE
    -   Auth : REQUIRED

```javascript
//axios

//request
axios
    .delete(
        "BASE_URL/blogs/7/",

        {
            headers: {
                //Token which you will get after login/signup
                Authorization: "Token e66628c5bb784e4b0c3366eecac938e18431ccbd",
            },
        }
    )
    .then((res) => {
        console.log(res.data);
    })
    .catch((err) => {
        console.log(err.response.data);
    });

//response
200;

//errors
{
    detail: "Authentication credentials were not provided.";
}
```

## like a blog

-   /likes/
    -   method : POST
    -   Auth : REQUIRED

```javascript
//axios

//request
axios
    .post(
        "BASE_URL/likes/",
        {
            post: 1,
        },
        {
            headers: {
                 //Token which you will get after login/signup
                Authorization: "Token e66628c5bb784e4b0c3366eecac938e18431ccbd",
            },
        }
    )
    .then((res) => {
        console.log(res.data);
    })
    .catch((err) => {
        console.log(err.response.data);
    });
//response
{
  id: 7,
  post: 1,
  liked_by: 4,
  liked_at: '2020-09-26T06:20:08.152535Z'
}

//error
{
    error: 'already liked'
},
{
    detail: "Authentication credentials were not provided.";
}

```

## remove like

-   /likes/:like-id (Int)/
    -   method : POST
    -   Auth : REQUIRED

```javascript
//axios

//request
axios
    .delete(
        "BASE_URL/likes/7",

        {
            headers: {
                //Token which you will get after login/signup
                Authorization: "Token e66628c5bb784e4b0c3366eecac938e18431ccbd",
            },
        }
    )
    .then((res) => {
        console.log(res.data);
    })
    .catch((err) => {
        console.log(err.response.data);
    });
//response
OK;
//errors
{
    detail: "Authentication credentials were not provided.";
}
```

## comment a blog

-   /comments/
    -   method : POST
    -   Auth : REQUIRED

```javascript
//axios

//request
axios
    .post(
        "BASE_URL/comments/",
        {
            post: 1,
            text: "nice post",
        },

        {
            headers: {
                 //Token which you will get after login/signup
                Authorization: "Token e66628c5bb784e4b0c3366eecac938e18431ccbd",
            },
        }
    )
    .then((res) => {
        console.log(res.data);
    })
    .catch((err) => {
        console.log(err.response.data);
    });

//response
{
  id: 8,
  post: 1,
  text: 'nice post',
  commented_by: 4,
  commented_at: '2020-09-26T06:32:21.983423Z'
}

//errors
{
    detail: "Authentication credentials were not provided.";
}
```

## edit comment

-   /comments/:comment-id(Int)/
    -   method : PUT/PATCH
    -   Auth : REQUIRED

```javascript
//axios

//request
axios
    .patch(
        "BASE_URL/comments/8/",
        {
            text: "nice post edited",
        },

        {
            headers: {
                 //Token which you will get after login/signup
                Authorization: "Token e66628c5bb784e4b0c3366eecac938e18431ccbd",
            },
        }
    )
    .then((res) => {
        console.log(res.data);
    })
    .catch((err) => {
        console.log(err.response.data);
    });

//response
{
  id: 8,
  post: 1,
  text: 'nice post edited',
  commented_by: 4,
  commented_at: '2020-09-26T06:32:21.983423Z'
}

//errors
{
    detail: "Authentication credentials were not provided.";
}

```

## remove comment

-   /comments/:comment-id(Int)/
    -   method : PUT/PATCH
    -   Auth : REQUIRED

```javascript
//axios

//request
axios
    .delete(
        "BASE_URL/comments/8/",

        {
            headers: {
                //Token which you will get after login/signup
                Authorization: "Token e66628c5bb784e4b0c3366eecac938e18431ccbd",
            },
        }
    )
    .then((res) => {
        console.log(res.data);
    })
    .catch((err) => {
        console.log(err.response.data);
    });

//response
OK;

//errors
{
    detail: "Authentication credentials were not provided.";
}
```

## user

### get all users

-   /users/
    -   method : GET

```javascript
//axios

//request
axios
    .get("BASE_URL/users/")
    .then((res) => {
        console.log(res.data);
    })
    .catch((err) => {
        console.log(err.response.data);
    });

//response
{
  count: 6,
  next: null,
  previous: null,
  results: [
    {
      id: 1,
      username: 'shreyashc',
      email: 'shreyashc@gmail.com',
      bio: null
    },
    {
        id: 2,
        username: 'manu',
        email: 'manu@gmail.com',
        bio: null
    },
    {
         id: 3,
         username: 'rahul',
         email: 'rahul@gmail.com',
         bio: null
    },
    {
      id: 4,
      username: 'shreyas',
      email: 'newEmail@gmail.com',
      bio: 'bio update'
    },
    {
      id: 5,
      username: 'shreyasf',
      email: 'shreyas@gmailf.com',
      bio: null
    },
    ...
    ...
    ...
  ]
```

### get a single user

-   /users/user-id (Int)/
    -   method : GET

```javascript
//axios

//request
axios
    .get("BASE_URL/users/3/")
    .then((res) => {
        console.log(res.data);
    })
    .catch((err) => {
        console.log(err.response.data);
    });

//response
{
    id: 3,
    username: "rahul",
    email: "rahul@gmail.com",
    bio: null,
};
```

## pagination

`all responses are paginated by default`

```javascript
{
    "count": 21,
    "next": "BASE_URL/comments/?page=2",
    "previous": null,
    "results": [res...]
}
```

-   count = total results

-   next = next page

-   previous = previous page

-   you can use query param **page**=page_no get get a specific page.

## search blogs

-   /search/?search=blog-title/
    -   method : GET

## search users

## filter blogs by category

-   GET /blogs/?category=category-name

## filter blogs by username

-   GET /blogs/?username=user-name

## filter blogs by userId

-   GET /blogs/?username=user-id

# additional info

## Uploading image for thumbnail

```javascript
axios
    .post("BASE_URL/blogs/",
    {
        //form-data
    },
    {
    headers: {
        Authorization: "Token e66628c5bb784e4b0c3366eecac938e18431ccbd",
        Content-Type: "multipart/form-data"
    },
    })
    .then((res) => {
        console.log(res.data);
    })
    .catch((err) => {
        console.log(err.response.data);
    });
```
