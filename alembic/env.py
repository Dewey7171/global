from logging.config import fileConfig

from sqlalchemy import create_engine, pool
from alembic import context
from app.models import Base
from app.database import DATABASE_URL  # DB URL 가져오기

# Alembic 설정 객체
config = context.config

# 로깅 설정 적용
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# 데이터베이스 메타데이터 지정
target_metadata = Base.metadata

def run_migrations_offline() -> None:
    """오프라인 모드에서 마이그레이션 실행"""
    url = DATABASE_URL.replace("asyncpg", "psycopg2")  # 동기 드라이버로 변환
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    """온라인 모드에서 마이그레이션 실행"""
    engine = create_engine(DATABASE_URL.replace("asyncpg", "psycopg2"), poolclass=pool.NullPool)

    with engine.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
