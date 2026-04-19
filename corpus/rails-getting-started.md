# Getting Started with Rails — Ruby on Rails Guides
Skip to main content

**More at rubyonrails.org:** More Ruby on Rails 
*   Blog
*   Guides
*   API
*   Forum
*   Contribute on GitHub

GuidesVersion: pick from the list to go to that Rails version's guides 

*   Home
*   Guides Index* * *

Start HereGetting Started with RailsInstall Ruby on Rails ModelsActive Record BasicsActive Record MigrationsActive Record ValidationsActive Record CallbacksActive Record AssociationsActive Record Query InterfaceActive Model Basics ViewsAction View OverviewLayouts and Rendering in RailsAction View HelpersAction View Form Helpers ControllersAction Controller OverviewAction Controller Advanced TopicsRails Routing from the Outside In Other ComponentsActive Support Core ExtensionsAction Mailer BasicsAction Mailbox BasicsAction Text OverviewActive Job BasicsActive Storage OverviewAction Cable Overview Digging DeeperRails Internationalization (I18n) APITesting Rails ApplicationsDebugging Rails ApplicationsConfiguring Rails ApplicationsThe Rails Command LineThe Asset PipelineWorking with JavaScript in RailsAutoloading and ReloadingUsing Rails for API-only Applications Going to ProductionTuning Performance for DeploymentCaching with Rails: An OverviewSecuring Rails ApplicationsError Reporting in Rails Applications Advanced Active RecordMultiple DatabasesActive Record EncryptionComposite Primary Keys Extending RailsThe Basics of Creating Rails PluginsRails on RackCreating and Customizing Rails Generators & Templates ContributingContributing to Ruby on RailsAPI Documentation GuidelinesGuides GuidelinesInstalling Rails Core Development Dependencies PoliciesMaintenance Policy Release NotesUpgrading Ruby on RailsVersion 8.1 - October 2025Version 8.0 - November 2024Version 7.2 - August 2024Version 7.1 - October 2023Version 7.0 - December 2021Version 6.1 - December 2020Version 6.0 - August 2019Version 5.2 - April 2018Version 5.1 - April 2017Version 5.0 - June 2016Version 4.2 - December 2014Version 4.1 - April 2014Version 4.0 - June 2013Version 3.2 - January 2012Version 3.1 - August 2011Version 3.0 - August 2010Version 2.3 - March 2009Version 2.2 - November 2008  
*   Contribute
*    Navigate to a guide:  

* * *

# Getting Started with Rails

This guide covers getting up and running with Ruby on Rails.

After reading this guide, you will know:

*   How to install Rails, create a new Rails application, and connect your application to a database.
*   The general layout of a Rails application.
*   The basic principles of MVC (Model, View, Controller) and RESTful design.
*   How to quickly generate the starting pieces of a Rails application.
*   How to deploy your app to production using Kamal.

Skip to article body
##  Chapters

1.   Introduction
2.   Rails Philosophy
3.   Creating a New Rails App
    *   Prerequisites
    *   Creating Your First Rails App
    *   Directory Structure
    *   Model-View-Controller Basics

4.   Hello, Rails!
    *   Autoloading in Development

5.   Creating a Database Model
    *   Database Migrations
    *   Running Migrations

6.   Rails Console
7.   Active Record Model Basics
    *   Creating Records
    *   Querying Records
    *   Filtering & Ordering Records
    *   Finding Records
    *   Updating Records
    *   Deleting Records
    *   Validations

8.   A Request's Journey Through Rails
9.   Routes
    *   Parts of a URL
    *   HTTP Methods and Their Purpose
    *   Rails Routes
    *   Routes Command

10.   Controllers & Actions
    *   Making Requests
    *   Instance Variables
    *   CRUD Actions
    *   Showing Individual Products
    *   Creating Products
    *   Editing Products
    *   Deleting Products

11.   Adding Authentication
    *   Adding Log Out
    *   Allowing Unauthenticated Access
    *   Showing Links for Authenticated Users Only

12.   Caching Products
13.   Rich Text Fields with Action Text
14.   File Uploads with Active Storage
15.   Internationalization (I18n)
16.   Action Mailer and Email Notifications
    *   Basic Inventory Tracking
    *   Adding Subscribers to Products
    *   In Stock Email Notifications
    *   Extracting a Concern
    *   Unsubscribe Links

17.   Adding CSS & JavaScript
    *   Propshaft
    *   Import Maps
    *   Hotwire

18.   Testing
    *   Fixtures
    *   Testing Emails

19.   Consistently Formatted Code with RuboCop
20.   Security
21.   Continuous Integration with GitHub Actions
22.   Deploying to Production
    *   Adding a User to Production
    *   Background Jobs using Solid Queue

23.   What's Next?

## 1. Introduction

Welcome to Ruby on Rails! In this guide, we'll walk through the core concepts of building web applications with Rails. You don't need any experience with Rails to follow along with this guide.

Rails is a web framework built for the Ruby programming language. Rails takes advantage of many features of Ruby so we **strongly** recommend learning the basics of Ruby so that you understand some of the basic terms and vocabulary you will see in this tutorial.

*   Official Ruby Programming Language website
*   List of Free Programming Books

## 2. Rails Philosophy

Rails is a web application development framework written in the Ruby programming language. It is designed to make programming web applications easier by making assumptions about what every developer needs to get started. It allows you to write less code while accomplishing more than many other languages and frameworks. Experienced Rails developers also report that it makes web application development more fun.

Rails is opinionated software. It makes the assumption that there is a "best" way to do things, and it's designed to encourage that way - and in some cases to discourage alternatives. If you learn "The Rails Way" you'll probably discover a tremendous increase in productivity. If you persist in bringing old habits from other languages to your Rails development, and trying to use patterns you learned elsewhere, you may have a less happy experience.

The Rails philosophy includes two major guiding principles:

*   **Don't Repeat Yourself:** DRY is a principle of software development which states that "Every piece of knowledge must have a single, unambiguous, authoritative representation within a system". By not writing the same information over and over again, our code is more maintainable, more extensible, and less buggy.
*   **Convention Over Configuration:** Rails has opinions about the best way to do many things in a web application, and defaults to this set of conventions, rather than require that you define them yourself through endless configuration files.

## 3. Creating a New Rails App

We're going to build a project called `store` - a simple e-commerce app that demonstrates several of Rails' built-in features.

Any commands prefaced with a dollar sign `$` should be run in the terminal.

### 3.1. Prerequisites

For this project, you will need:

*   Ruby 3.2 or newer
*   Rails 8.1.0 or newer
*   A code editor

Follow the Install Ruby on Rails Guide if you need to install Ruby and/or Rails.

Let's verify the correct version of Rails is installed. To display the current version, open a terminal and run the following. You should see a version number printed out:

```
$ rails --version
Rails 8.1.0
```
Copy

The version shown should be Rails 8.1.0 or higher.

### 3.2. Creating Your First Rails App

Rails comes with several commands to make life easier. Run `rails --help` to see all of the commands.

`rails new` generates the foundation of a fresh Rails application for you, so let's start there.

To create our `store` application, run the following command in your terminal:

```
$ rails new store
```
Copy

You can customize the application Rails generates by using flags. To see these options, run `rails new --help`.

After your new application is created, switch to its directory:

```
$ cd store
```
Copy

### 3.3. Directory Structure

Let's take a quick glance at the files and directories that are included in a new Rails application. You can open this folder in your code editor or run `ls -la` in your terminal to see the files and directories.

| File/Folder | Purpose |
| --- | --- |
| app/ | Contains the controllers, models, views, helpers, mailers, jobs, and assets for your application. **You'll focus mostly on this folder for the remainder of this guide.** |
| bin/ | Contains the `rails` script that starts your app and can contain other scripts you use to set up, update, deploy, or run your application. |
| config/ | Contains configuration for your application's routes, database, and more. This is covered in more detail in Configuring Rails Applications. |
| config.ru | Rack configuration for Rack-based servers used to start the application. |
| db/ | Contains your current database schema, as well as the database migrations. |
| Dockerfile | Configuration file for Docker. |
| Gemfile Gemfile.lock | These files allow you to specify what gem dependencies are needed for your Rails application. These files are used by the Bundler gem. |
| lib/ | Extended modules for your application. |
| log/ | Application log files. |
| public/ | Contains static files and compiled assets. When your app is running, this directory will be exposed as-is. |
| Rakefile | This file locates and loads tasks that can be run from the command line. The task definitions are defined throughout the components of Rails. Rather than changing `Rakefile`, you should add your own tasks by adding files to the `lib/tasks` directory of your application. |
| README.md | This is a brief instruction manual for your application. You should edit this file to tell others what your application does, how to set it up, and so on. |
| script/ | Contains one-off or general purpose scripts and benchmarks. |
| storage/ | Contains SQLite databases and Active Storage files for Disk Service. This is covered in Active Storage Overview. |
| test/ | Unit tests, fixtures, and other test apparatus. These are covered in Testing Rails Applications. |
| tmp/ | Temporary files (like cache and pid files). |
| vendor/ | A place for all third-party code. In a typical Rails application this includes vendored gems. |
| .dockerignore | This file tells Docker which files it should not copy into the container. |
| .gitattributes | This file defines metadata for specific paths in a Git repository. This metadata can be used by Git and other tools to enhance their behavior. See the gitattributes documentation for more information. |
| .git/ | Contains Git repository files. |
| .github/ | Contains GitHub specific files. |
| .gitignore | This file tells Git which files (or patterns) it should ignore. See GitHub - Ignoring files for more information about ignoring files. |
| .kamal/ | Contains Kamal secrets and deployment hooks. |
| .rubocop.yml | This file contains the configuration for RuboCop. |
| .ruby-version | This file contains the default Ruby version. |

### 3.4. Model-View-Controller Basics

Rails code is organized using the Model-View-Controller (MVC) architecture. With MVC, we have three main concepts where the majority of our code lives:

*   Model - Manages the data in your application. Typically, your database tables.
*   View - Handles rendering responses in different formats like HTML, JSON, XML, etc.
*   Controller - Handles user interactions and the logic for each request.

Now that we've got a basic understanding of MVC, let's see how it's used in Rails.

## 4. Hello, Rails!

Let's start easy by creating our application's database and boot up our Rails server for the first time.

In your terminal, run the following commands in the `store` directory:

```
$ bin/rails db:create
```
Copy

This will initially create the application's database.

```
$ bin/rails server
```
Copy

When we run commands inside an application directory, we should use `bin/rails`. This makes sure the application's version of Rails is used.

This will start up a web server called Puma that will serve static files and your Rails application:

```
=> Booting Puma
=> Rails 8.1.0 application starting in development
=> Run `bin/rails server --help` for more startup options
Puma starting in single mode...
* Puma version: 6.4.3 (ruby 3.3.5-p100) ("The Eagle of Durango")
*  Min threads: 3
*  Max threads: 3
*  Environment: development
*          PID: 12345
* Listening on http://127.0.0.1:3000
* Listening on http://[::1]:3000
Use Ctrl-C to stop
```
Copy

To see your Rails application, open http://localhost:3000 in your browser. You will see the default Rails welcome page:

It works!

This page is the _smoke test_ for a new Rails application, ensuring that everything is working behind the scenes to serve a page.

To stop the Rails server anytime, press `Ctrl-C` in your terminal.

### 4.1. Autoloading in Development

Developer happiness is a cornerstone philosophy of Rails and one way of achieving this is with automatic code reloading in development.

Once you start the Rails server, new files or changes to existing files are detected and automatically loaded or reloaded as necessary. This allows you to focus on building without having to restart your Rails server after every change.

You may also notice that Rails applications rarely use `require` statements like you may have seen in other programming languages. Rails uses naming conventions to require files automatically so you can focus on writing your application code.

See Autoloading and Reloading Constants for more details.

## 5. Creating a Database Model

Active Record is a feature of Rails that maps relational databases to Ruby code. It helps generate the structured query language (SQL) for interacting with the database like creating, updating, and deleting tables and records. Our application is using SQLite which is the default for Rails.

Let's start by adding a database table to our Rails application to add products to our simple e-commerce store.

```
$ bin/rails generate model Product name:string
```
Copy

This command tells Rails to generate a model named `Product` which has a `name` column and type of `string` in the database. Later on, you'll learn how to add other column types.

You'll see the following in your terminal:

```
invoke  active_record
      create    db/migrate/20240426151900_create_products.rb
      create    app/models/product.rb
      invoke    test_unit
      create      test/models/product_test.rb
      create      test/fixtures/products.yml
```
Copy

This command does several things. It creates...

1.   A migration in the `db/migrate` folder.
2.   An Active Record model in `app/models/product.rb`.
3.   Tests and test fixtures for this model.

Model names are _singular_, because an instantiated model represents a single record in the database (i.e., You are creating a _product_ to add to the database.).

### 5.1. Database Migrations

A _migration_ is a set of changes we want to make to our database.

By defining migrations, we're telling Rails how to change the database to add, change, or remove tables, columns or other attributes of our database. This helps keep track of changes we make in development (only on our computer) so they can be deployed to production (live, online!) safely.

In your code editor, open the migration Rails created for us so we can see what the migration does.

As convention we'll state the filepath as a comment on top of each file

```
# db/migrate/<timestamp>_create_products.rb
class CreateProducts < ActiveRecord::Migration[8.1]
  def change
    create_table :products do |t|
      t.string :name

      t.timestamps
    end
  end
end
```
Copy

This migration is telling Rails to create a new database table named `products`.

In contrast to the model above, Rails makes the database table names _plural_, because the database holds all of the instances of each model (i.e., You are creating a database of _products_).

The `create_table` block then defines which columns and types should be defined in this database table.

`t.string :name` tells Rails to create a column in the `products` table called `name` and set the type as `string`.

`t.timestamps` is a shortcut for defining two columns on your models: `created_at:datetime` and `updated_at:datetime`. You'll see these columns on most Active Record models in Rails and they are automatically set by Active Record when creating or updating records.

### 5.2. Running Migrations

Now that you have defined what changes to make to the database, use the following command to run the migrations:

```
$ bin/rails db:migrate
```
Copy

This command checks for any new migrations and applies them to your database. Its output looks like this:

```
== 20240426151900 CreateProducts: migrating ===================================
-- create_table(:products)
   -> 0.0030s
== 20240426151900 CreateProducts: migrated (0.0031s) ==========================
```
Copy

If you make a mistake, you can run `bin/rails db:rollback` to undo the last migration.

## 6. Rails Console

Now that we have created our products table, we can interact with it in Rails. Let's try it out.

For this, we're going to use a Rails feature called the _console_. The console is a helpful, interactive tool for testing our code in our Rails application.

```
$ bin/rails console
```
Copy

You will be presented with a prompt like the following:

```
Loading development environment (Rails 8.1.0)
store(dev)>
```
Copy

Here we can type code that will be executed when we hit `Enter`. Let's try printing out the Rails version:

```
store(dev)> Rails.version
=> "8.1.0"
```
Copy

It works!

## 7. Active Record Model Basics

When we ran the Rails model generator to create the `Product` model, it created a file at `app/models/product.rb`. This file creates a class that uses Active Record for interacting with our `products` database table.

```
# app/models/product.rb
class Product < ApplicationRecord
end
```
Copy

You might be surprised that there is no code in this class. How does Rails know what defines this model?

When the `Product` model is used, Rails will query the database table for the column names and types and automatically generate code for these attributes. Rails saves us from writing this boilerplate code and instead takes care of it for us behind the scenes so we can focus on our application logic instead.

Let's use the Rails console to see what columns Rails detects for the Product model.

Run:

```
store(dev)> Product.column_names
```
Copy

And you should see:

```
=> ["id", "name", "created_at", "updated_at"]
```
Copy

Rails asked the database for column information above and used that information to define attributes on the `Product` class dynamically so you don't have to manually define each of them. This is one example of how Rails makes development a breeze.

### 7.1. Creating Records

We can instantiate a new Product record with the following code:

```
store(dev)> product = Product.new(name: "T-Shirt")
=> #<Product:0x000000012e616c30 id: nil, name: "T-Shirt", created_at: nil, updated_at: nil>
```
Copy

The `product` variable is an instance of `Product`. It has not been saved to the database, and so does not have an ID, created_at, or updated_at timestamps.

We can call `save` to write the record to the database.

```
store(dev)> product.save
  TRANSACTION (0.1ms)  BEGIN immediate TRANSACTION /*application='Store'*/
  Product Create (0.9ms)  INSERT INTO "products" ("name", "created_at", "updated_at") VALUES ('T-Shirt', '2024-11-09 16:35:01.117836', '2024-11-09 16:35:01.117836') RETURNING "id" /*application='Store'*/
  TRANSACTION (0.9ms)  COMMIT TRANSACTION /*application='Store'*/
=> true
```
Copy

When `save` is called, Rails takes the attributes in memory and generates an `INSERT` SQL query to insert this record into the database.

Rails also updates the object in memory with the database record `id` along with the `created_at` and `updated_at` timestamps. We can see that by printing out the `product` variable.

```
store(dev)> product
=> #<Product:0x00000001221f6260 id: 1, name: "T-Shirt", created_at: "2024-11-09 16:35:01.117836000 +0000", updated_at: "2024-11-09 16:35:01.117836000 +0000">
```
Copy

Similar to `save`, we can use `create` to instantiate and save an Active Record object in a single call.

```
store(dev)> Product.create(name: "Pants")
  TRANSACTION (0.1ms)  BEGIN immediate TRANSACTION /*application='Store'*/
  Product Create (0.4ms)  INSERT INTO "products" ("name", "created_at", "updated_at") VALUES ('Pants', '2024-11-09 16:36:01.856751', '2024-11-09 16:36:01.856751') RETURNING "id" /*application='Store'*/
  TRANSACTION (0.1ms)  COMMIT TRANSACTION /*application='Store'*/
=> #<Product:0x0000000120485c80 id: 2, name: "Pants", created_at: "2024-11-09 16:36:01.856751000 +0000", updated_at: "2024-11-09 16:36:01.856751000 +0000">
```
Copy

### 7.2. Querying Records

We can also look up records from the database using our Active Record model.

To find all the Product records in the database, we can use the `all` method. This is a _class_ method, which is why we can use it on Product (versus an instance method that we would call on the product instance, like `save` above).

```
store(dev)> Product.all
  Product Load (0.1ms)  SELECT "products".* FROM "products" /* loading for pp */ LIMIT 11 /*application='Store'*/
=> [#<Product:0x0000000121845158 id: 1, name: "T-Shirt", created_at: "2024-11-09 16:35:01.117836000 +0000", updated_at: "2024-11-09 16:35:01.117836000 +0000">,
 #<Product:0x0000000121845018 id: 2, name: "Pants", created_at: "2024-11-09 16:36:01.856751000 +0000", updated_at: "2024-11-09 16:36:01.856751000 +0000">]
```
Copy

This generates a `SELECT` SQL query to load all records from the `products` table. Each record is automatically converted into an instance of our Product Active Record model so we can easily work with them from Ruby.

The `all` method returns an `ActiveRecord::Relation` object which is an Array-like collection of database records with features to filter, sort, and execute other database operations.

### 7.3. Filtering & Ordering Records

What if we want to filter the results from our database? We can use `where` to filter records by a column.

```
store(dev)> Product.where(name: "Pants")
  Product Load (1.5ms)  SELECT "products".* FROM "products" WHERE "products"."name" = 'Pants' /* loading for pp */ LIMIT 11 /*application='Store'*/
=> [#<Product:0x000000012184d858 id: 2, name: "Pants", created_at: "2024-11-09 16:36:01.856751000 +0000", updated_at: "2024-11-09 16:36:01.856751000 +0000">]
```
Copy

This generates a `SELECT` SQL query but also adds a `WHERE` clause to filter the records that have a `name` matching `"Pants"`. This also returns an `ActiveRecord::Relation` because multiple records may have the same name.

We can use `order(name: :asc)` to sort records by name in ascending alphabetical order.

```
store(dev)> Product.order(name: :asc)
  Product Load (0.3ms)  SELECT "products".* FROM "products" /* loading for pp */ ORDER BY "products"."name" ASC LIMIT 11 /*application='Store'*/
=> [#<Product:0x0000000120e02a88 id: 2, name: "Pants", created_at: "2024-11-09 16:36:01.856751000 +0000", updated_at: "2024-11-09 16:36:01.856751000 +0000">,
 #<Product:0x0000000120e02948 id: 1, name: "T-Shirt", created_at: "2024-11-09 16:35:01.117836000 +0000", updated_at: "2024-11-09 16:35:01.117836000 +0000">]
```
Copy

### 7.4. Finding Records

What if we want to find one specific record?

We can do this by using the `find` class method to look up a single record by ID. Call the method and pass in the specific ID by using the following code:

```
store(dev)> Product.find(1)
  Product Load (0.2ms)  SELECT "products".* FROM "products" WHERE "products"."id" = 1 LIMIT 1 /*application='Store'*/
=> #<Product:0x000000012054af08 id: 1, name: "T-Shirt", created_at: "2024-11-09 16:35:01.117836000 +0000", updated_at: "2024-11-09 16:35:01.117836000 +0000">
```
Copy

This generates a `SELECT` query but specifies a `WHERE` for the `id` column matching the ID of `1` that was passed in. It also adds a `LIMIT` to only return a single record.

This time, we get a `Product` instance instead of an `ActiveRecord::Relation` since we're only retrieving a single record from the database.

### 7.5. Updating Records

Records can be updated in 2 ways: using `update` or assigning attributes and calling `save`.

We can call `update` on a Product instance and pass in a Hash of new attributes to save to the database. This will assign the attributes, run validations, and save the changes to the database in one method call.

```
store(dev)> product = Product.find(1)
store(dev)> product.update(name: "Shoes")
  TRANSACTION (0.1ms)  BEGIN immediate TRANSACTION /*application='Store'*/
  Product Update (0.3ms)  UPDATE "products" SET "name" = 'Shoes', "updated_at" = '2024-11-09 22:38:19.638912' WHERE "products"."id" = 1 /*application='Store'*/
  TRANSACTION (0.4ms)  COMMIT TRANSACTION /*application='Store'*/
=> true
```
Copy

This updated the name of the "T-Shirt" product to "Shoes" in the database. Confirm this by running `Product.all` again.

```
store(dev)> Product.all
```
Copy

You will see two products: Shoes and Pants.

```
Product Load (0.3ms)  SELECT "products".* FROM "products" /* loading for pp */ LIMIT 11 /*application='Store'*/
=>
[#<Product:0x000000012c0f7300
  id: 1,
  name: "Shoes",
  created_at: "2024-12-02 20:29:56.303546000 +0000",
  updated_at: "2024-12-02 20:30:14.127456000 +0000">,
 #<Product:0x000000012c0f71c0
  id: 2,
  name: "Pants",
  created_at: "2024-12-02 20:30:02.997261000 +0000",
  updated_at: "2024-12-02 20:30:02.997261000 +0000">]
```
Copy

Alternatively, we can assign attributes and call `save` when we're ready to validate and save changes to the database.

Let's change the name "Shoes" back to "T-Shirt".

```
store(dev)> product = Product.find(1)
store(dev)> product.name = "T-Shirt"
=> "T-Shirt"
store(dev)> product.save
  TRANSACTION (0.1ms)  BEGIN immediate TRANSACTION /*application='Store'*/
  Product Update (0.2ms)  UPDATE "products" SET "name" = 'T-Shirt', "updated_at" = '2024-11-09 22:39:09.693548' WHERE "products"."id" = 1 /*application='Store'*/
  TRANSACTION (0.0ms)  COMMIT TRANSACTION /*application='Store'*/
=> true
```
Copy

### 7.6. Deleting Records

The `destroy` method can be used to delete a record from the database.

```
store(dev)> product.destroy
  TRANSACTION (0.1ms)  BEGIN immediate TRANSACTION /*application='Store'*/
  Product Destroy (0.4ms)  DELETE FROM "products" WHERE "products"."id" = 1 /*application='Store'*/
  TRANSACTION (0.1ms)  COMMIT TRANSACTION /*application='Store'*/
=> #<Product:0x0000000125813d48 id: 1, name: "T-Shirt", created_at: "2024-11-09 22:39:38.498730000 +0000", updated_at: "2024-11-09 22:39:38.498730000 +0000">
```
Copy

This deleted the T-Shirt product from our database. We can confirm this with `Product.all` to see that it only returns Pants.

```
store(dev)> Product.all
  Product Load (1.9ms)  SELECT "products".* FROM "products" /* loading for pp */ LIMIT 11 /*application='Store'*/
=>
[#<Product:0x000000012abde4c8
  id: 2,
  name: "Pants",
  created_at: "2024-11-09 22:33:19.638912000 +0000",
  updated_at: "2024-11-09 22:33:19.638912000 +0000">]
```
Copy

### 7.7. Validations

Active Record provides _validations_ which allows you to ensure data inserted into the database adheres to certain rules.

Let's add a `presence` validation to the Product model to ensure that all products must have a `name`.

```
# app/models/product.rb
class Product < ApplicationRecord
  validates :name, presence: true
end
```
Copy

You might remember that Rails automatically reloads changes during development. However, if the console is running when you make updates to the code, you'll need to manually refresh it. So let's do this now by running 'reload!'.

```
store(dev)> reload!
Reloading...
```
Copy

Let's try to create a Product without a name in the Rails console.

```
store(dev)> product = Product.new
store(dev)> product.save
=> false
```
Copy

This time `save` returns `false` because the `name` attribute wasn't specified.

Rails automatically runs validations during create, update, and save operations to ensure valid input. To see a list of errors generated by validations, we can call `errors` on the instance.

```
store(dev)> product.errors
=> #<ActiveModel::Errors [#<ActiveModel::Error attribute=name, type=blank, options={}>]>
```
Copy

This returns an `ActiveModel::Errors` object that can tell us exactly which errors are present.

It also can generate friendly error messages for us that we can use in our user interface.

```
store(dev)> product.errors.full_messages
=> ["Name can't be blank"]
```
Copy

Now let's build a web interface for our Products.

We are done with the console for now, so you can exit out of it by running `exit`.

## 8. A Request's Journey Through Rails

To get Rails saying "Hello", you need to create at minimum a _route_, a _controller_ with an _action_, and a _view_. A route maps a request to a controller action. A controller action performs the necessary work to handle the request, and prepares any data for the view. A view displays data in a desired format.

In terms of implementation: Routes are rules written in a Ruby DSL (Domain-Specific Language). Controllers are Ruby classes, and their public methods are actions. And views are templates, usually written in a mixture of HTML and Ruby.

That's the short of it, but we’re going to walk through each of these steps in more detail next.

## 9. Routes

In Rails, a route is the part of the URL that determines how an incoming HTTP request is directed to the appropriate controller and action for processing. First, let's do a quick refresher on URLs and HTTP Request methods.

### 9.1. Parts of a URL

Let's examine the different parts of a URL:

```
https://example.org/products?sale=true&sort=asc
```
Copy

In this URL,each part has a name:

*   `https` is the **protocol**
*   `example.org` is the **host**
*   `/products` is the **path**
*   `?sale=true&sort=asc` are the **query parameters**

### 9.2. HTTP Methods and Their Purpose

HTTP requests use methods to tell a server what action it should perform for a given URL. Here are the most common methods:

*   A `GET` request tells the server to retrieve the data for a given URL (e.g., loading a page or fetching a record).
*   A `POST` request will submit data to the URL for processing (usually creating a new record).
*   A `PUT` or `PATCH` request submits data to a URL to update an existing record.
*   A `DELETE` request to a URL tells the server to delete a record.

### 9.3. Rails Routes

A `route` in Rails refers to a line of code that pairs an HTTP Method and a URL path. The route also tells Rails which `controller` and `action` should respond to a request.

To define a route in Rails, let's go back to your code editor and add the following route to `config/routes.rb`

```
# config/routes.rb
Rails.application.routes.draw do
  # ...
  get "/products", to: "products#index"
end
```
Copy

This route tells Rails to look for GET requests to the `/products` path. In this example, we specified `"products#index"` for where to route the request.

When Rails sees a request that matches, it will send the request to the `ProductsController` and the `index` action inside of that controller. This is how Rails will process the request and return a response to the browser.

You'll notice that we don't need to specify the protocol, domain, or query params in our routes. That's basically because the protocol and domain make sure the request reaches your server. From there, Rails picks up the request and knows which path to use for responding to the request based on what routes are defined. The query params are like options that Rails can use to apply to the request, so they are typically used in the controller for filtering the data.

Let's look at another example. Add this line after the previous route:

```
# config/routes.rb
Rails.application.routes.draw do
  # ...
  get "/products", to: "products#index"
  post "/products", to: "products#create"
end
```
Copy

Here, we've told Rails to take POST requests to "/products" and process them with the `ProductsController` using the `create` action.

Routes may also need to match URLs with certain patterns. So how does that work?

```
# config/routes.rb
Rails.application.routes.draw do
  # ...
  get "/products/:id", to: "products#show"
end
```
Copy

This route has `:id` in it. This is called a `parameter` and it captures a portion of the URL to be used later for processing the request.

If a user visits `/products/1`, the `:id` param is set to `1` and can be used in the controller action to look up and display the Product record with an ID of 1. `/products/2` would display Product with an ID of 2 and so on.

Route parameters don't have to be Integers, either.

For example, you could have a blog with articles and match `/blog/hello-world` with the following route:

```
# config/routes.rb
Rails.application.routes.draw do
  # ...
  get "/blog/:title", to: "blog#show"
end
```
Copy

Rails will capture `hello-world` out of `/blog/hello-world` and this can be used to look up the blog post with the matching title.

#### 9.3.1. CRUD Routes

There are 4 common actions you will generally need for a resource: Create, Read, Update, Delete (CRUD). This translates to 8 typical routes:

*   Index - Shows all the records
*   New - Renders a form for creating a new record
*   Create - Processes the new form submission, handling errors and creating the record
*   Show - Renders a specific record for viewing
*   Edit - Renders a form for updating a specific record
*   Update (full) - Handles the edit form submission, handling errors and updating the entire record, and typically triggered by a PUT request.
*   Update (partial) - Handles the edit form submission, handling errors and updating specific attributes of the record, and typically triggered by a PATCH request.
*   Destroy - Handles deleting a specific record

We can add routes for these CRUD actions with the following:

```
# config/routes.rb
Rails.application.routes.draw do
  # ...
  get "/products", to: "products#index"

  get "/products/new", to: "products#new"
  post "/products", to: "products#create"

  get "/products/:id", to: "products#show"

  get "/products/:id/edit", to: "products#edit"
  patch "/products/:id", to: "products#update"
  put "/products/:id", to: "products#update"

  delete "/products/:id", to: "products#destroy"
end
```
Copy

#### 9.3.2. Resource Routes

Typing out these routes every time is redundant, so Rails provides a shortcut for defining them. To create all of the same CRUD routes, replace the above routes with this single line:

```
# config/routes.rb
Rails.application.routes.draw do
  # ...
  resources :products
end
```
Copy

If you don’t want all these CRUD actions, you specify exactly what you need. Check out the routing guide for details.

### 9.4. Routes Command

Rails provides a command that displays all the routes your application responds to.

In your terminal, run the following command.

```
$ bin/rails routes
```
Copy

You'll see this in the output which are the routes generated by `resources :products`

```
Prefix Verb   URI Pattern                  Controller#Action
    products GET    /products(.:format)          products#index
             POST   /products(.:format)          products#create
 new_product GET    /products/new(.:format)      products#new
edit_product GET    /products/:id/edit(.:format) products#edit
     product GET    /products/:id(.:format)      products#show
             PATCH  /products/:id(.:format)      products#update
             PUT    /products/:id(.:format)      products#update
             DELETE /products/:id(.:format)      products#destroy
```
Copy

You'll also see routes from other built-in Rails features like health checks.


---

*(Excerpt: rest of the guide truncated)*
