from Seeding import Seeding

class Developer(Seeding):
    def __init__(self, connection):
        super().__init__(connection)

    def get_all_email(self):
        self.cursor.execute("SELECT email FROM DEVELOPER")
        emails = [record[0] for record in self.cursor.fetchall()]
        return emails

    def get_all_username(self):
        self.cursor.execute("SELECT username FROM DEVELOPER")
        usernames = [record[0] for record in self.cursor.fetchall()]
        return usernames

    def seeding(self, num_records):
        for _ in range(num_records):
            email = self.generate_unique_email()
            username = self.generate_unique_username()
            password = self.fake.password()
            nama_depan = self.fake.first_name()
            nama_belakang = self.fake.last_name()
            tanggal_lahir = self.fake.date_of_birth()
            usia = self.calculate_age(tanggal_lahir)

            sql = "INSERT INTO DEVELOPER (email, username, password, nama_depan, nama_belakang, tanggal_lahir, usia) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            val = (email, username, password, nama_depan, nama_belakang, tanggal_lahir, usia)

            self.cursor.execute(sql, val)
            self.connection.commit()

    def generate_unique_email(self):
        email = self.fake.email()
        existing_emails = self.get_all_email()
        while email in existing_emails:
            email = self.fake.email()
        return email

    def generate_unique_username(self):
        username = self.fake.user_name()
        existing_usernames = self.get_all_username()
        while username in existing_usernames:
            username = self.fake.user_name()
        return username