2022-05-28
Reading a lot about fastAPI, looks good but lacks some conventions. Want to end up with something consistent but that doesn't require use of any sort of explicit mapping. Think I'll ripoff elixir and use core/model that will probably represent database models and core/model_web that will represent request/responses as naming conventions. Watheaver I ended up trying is naturally turning into some sort of command/handler pattern becuase the framework seem to work better this way.

Something I found later on while reading docs for setting up database is that what I called models_web is commonly known as schemas, howeaver I think elixir-like convention is clarer so I'll keep it this way.

I think the first part of endpoints is done, will focus on database now and then wire everything through a controller but I think this time I'll try to call it usecase.

2022-05-29
Today I start with database. DISCLAIMER: I don't like using ORMs, so I'll make raw queries into a model which in my opinion is much more fitting for any kind of application except for monoliths. This is because while ORMs add a desired level of decoupling from your datasource it feels like an unnecessary complexity for smaller applications like any sort of microservices.

A benefit from not relying on ORMs is that you'd either have to remap your db models to your core/models (in theory the best choice, but adds a lot of redundant code) or make de core/models depend your ORM (now you are coupled to a dependency). By not relying on ORMs it's possible to map your data from the source to models withouth relying on ORM code but on pure SQL.

Due to time constraints I'll skip migrations and do everything manually, might also skip controllers and make calls straight into the routes file.
Dealing with pgsql manually was a bit harder than mysql, but everything seems to be working for now. I need to define my core models and check if I can insert/retrieve assets before going back to users and deal with authentication. Also I'll be using numeric id over uuid so I can go faster with development. After that it should be a matter of setting up the rest of database and nescessary queries through the API, I want to be done with all the backend by the end of the day.

btw, I don't think I'll be adding authorization, only authentication.