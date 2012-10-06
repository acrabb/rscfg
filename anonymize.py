import json

email_hash = {}
email_pairs = {}
rand_emails = {}
recipient = ""
sender = ""
subject = ""
body_plain = ""




def randEmail():
        """creates a new random email
        using progressive ints. Checks
        for originality against rand_emails."""
        i = 0
        while i in rand_emails:
                i += 1
        rand_emails[i] = i
        newEmail = str(i) + "@routing.mailgun.org"
        return newEmail

def anonAndStore(address):
        """Hashes and stores the email
        of the sender to a dictionary,
        email_hash"""
        hashedEmail = hash(address)
        newEmail = randEmail()
        email_hash[hashedEmail] = address
        email_pairs[newEmail] = hashedEmail
        return newEmail

def retrieveEmail(address):
        """retrieves the original email address."""
        if address in email_pairs:
                hashedEmail = email_pairs[address]
                return email_hash[hashedEmail]
        else:
                return

def parseJson(jObject):
        parsed_data = json.dumps(jObject)
        recipient = parsed_data['recipient']
        sender = parsed_data['sender']
        subject = parsed_data['subject']
        body_plain = parsed_data['body-plain']
        return

if __name__ == "__main__":
        print('Look at the functions. We couldnt get it fully implemented but we were on our way.')
