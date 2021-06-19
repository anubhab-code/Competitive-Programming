def check_the_bucket(bucket):
    try:
        pos = bucket.index("gold")
    except:
        return False
    else:
        return True