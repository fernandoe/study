# Getting Started

## Steps

```bash

gem install rails
rails --version

rails new blog

bin/rails server

bin/rails generate controller Articles index --skip-routes

bin/rails generate model Article title:string body:text

bin/rails db:migrate

bin/rails console

```

```ruby
article = Article.new(title: "Hello Rails", body: "I am on Rails!")
article.save
article
Article.find(1)
Article.all
```

```bash
bin/rails routes

bin/rails generate model Comment commenter:string body:text article:references

bin/rails db:migrate

bin/rails generate controller Comments

bin/rails generate migration AddStatusToArticles status:string
bin/rails generate migration AddStatusToComments status:string

bin/rails db:migrate


```

