import pynecone as pc

config = pc.Config(
    app_name="getting_started_with_pynecone",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)
