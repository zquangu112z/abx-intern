import os
import redis
import pandas as pd
import zlib
import pickle


redis_client = redis.StrictRedis(
    host=os.environ.get("REDIS_HOST", "localhost"),
    port=os.environ.get("REDIS_PORT", "6379"),
    db=int(os.environ.get("REDIS_DB", "0"))
)


def main():
    df = pd.read_csv("misc/src/df_redis/data.csv")
    key = "my_df"
    redis_client.setex(
        key,
        18600,
        zlib.compress(pickle.dumps(df))
    )

    loaded_df = pickle.loads(zlib.decompress(
        redis_client.get(key)
    ))
    print(loaded_df.nlargest(n=1, columns="'CCS'"))


if __name__ == '__main__':
    main()
