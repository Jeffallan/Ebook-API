# Ebook API

The fast and easy API for all of your ebook needs.
Made with Python 3, Django Rest Framework, Scrapy and Docker

### Installing

Make sure ho have [Docker](https://docs.docker.com/v17.12/install/) and [Docker Compose](https://docs.docker.com/compose/install/) installed on your computer.

Navigate to the root directory of this project.

Make a copy of .modelenv and name it .env. Then fill in your desired environment variables (default values are suggested in .modelenv).

If you are running this project for the first time run the command:

`docker-compose -f docker-compose-build.yml up`

This will create a new PostgreSQL database and Django REST API (if they do not already exist).  This command also runs a Scrapy spider to populate the database.

If you want to restart the container and the database is populated, you can run:

`docker-compose -f docker-compose.yml up`


## Contributing

Individuals of all skill levels are welcome to contribute.


## License

This project is licensed under the GNU General Public License v3.0 License - see the [LICENSE.md](LICENSE.md) file for details
