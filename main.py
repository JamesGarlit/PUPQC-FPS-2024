from blueprints import initialize

app = initialize()

if __name__ == '__main__':
    app.run(debug=True)


# user.drop_table()
# print("Table created successfully...")
# Close the database connection
# user.close()