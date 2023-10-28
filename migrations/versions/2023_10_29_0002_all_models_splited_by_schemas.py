"""all models splited by schemas

Revision ID: 990bbcc25e31
Revises: 
Create Date: 2023-10-29 00:02:59.344839

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '990bbcc25e31'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('chat',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('chat_name', sa.String(), nullable=False),
    sa.Column('image', sa.String(), nullable=True),
    sa.Column('created_at', sa.TIMESTAMP(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    schema='chat'
    )
    op.create_table('ad_response',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_uuid', sa.UUID(), nullable=False),
    sa.Column('ad_id', sa.Integer(), nullable=False),
    sa.Column('status_id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    schema='response'
    )
    op.create_table('response_status',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('slug', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    schema='response'
    )
    op.create_table('privacy',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('slug', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    schema='settings'
    )
    op.create_table('user_privacy',
    sa.Column('user_uuid', sa.UUID(), nullable=False),
    sa.Column('privacy_id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('user_uuid', 'privacy_id'),
    schema='settings'
    )
    op.create_table('skill',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('slug', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    schema='skill'
    )
    op.create_table('speciality',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    schema='skill'
    )
    op.create_table('currency',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('slug', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    schema='subscription'
    )
    op.create_table('subscription_type',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('max_response_count', sa.Integer(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('currency_id', sa.Integer(), nullable=False),
    sa.Column('slug', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    schema='subscription'
    )
    op.create_table('team_permission',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('slug', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    schema='team'
    )
    op.create_table('contact_type',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('slug', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    schema='user'
    )
    op.create_table('role',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('slug', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    schema='user'
    )
    op.create_table('chat_member',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('chat_id', sa.Integer(), nullable=False),
    sa.Column('entity_uuid', sa.UUID(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(), nullable=False),
    sa.ForeignKeyConstraint(['chat_id'], ['chat.chat.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='chat'
    )
    op.create_table('sale',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('code', sa.String(), nullable=False),
    sa.Column('date_start', sa.DATE(), nullable=True),
    sa.Column('date_end', sa.DATE(), nullable=False),
    sa.Column('percent', sa.Integer(), nullable=False),
    sa.Column('subscription_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['subscription_id'], ['subscription.subscription_type.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='subscription'
    )
    op.create_table('user',
    sa.Column('uuid', sa.UUID(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('lastname', sa.String(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('hashed_password', sa.String(), nullable=False),
    sa.Column('is_verified', sa.Boolean(), nullable=False),
    sa.Column('role_id', sa.Integer(), nullable=False),
    sa.Column('image', sa.String(), nullable=True),
    sa.Column('location', sa.JSON(), nullable=True),
    sa.Column('sex', sa.String(), nullable=True),
    sa.Column('birthday', sa.TIMESTAMP(), nullable=True),
    sa.Column('created_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('deleted_at', sa.TIMESTAMP(), nullable=True),
    sa.Column('is_blocked', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['role_id'], ['user.role.id'], ),
    sa.PrimaryKeyConstraint('uuid'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username'),
    sa.UniqueConstraint('uuid'),
    schema='user'
    )
    op.create_table('message',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('chat_id', sa.Integer(), nullable=False),
    sa.Column('member_id', sa.Integer(), nullable=False),
    sa.Column('text', sa.Text(), nullable=True),
    sa.Column('created_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('deleted_at', sa.TIMESTAMP(), nullable=True),
    sa.ForeignKeyConstraint(['chat_id'], ['chat.chat.id'], ),
    sa.ForeignKeyConstraint(['member_id'], ['chat.chat_member.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='chat'
    )
    op.create_table('settings',
    sa.Column('user_uuid', sa.UUID(), nullable=False),
    sa.Column('is_notifying', sa.Boolean(), nullable=False),
    sa.Column('is_mailing', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['user_uuid'], ['user.user.uuid'], ),
    sa.PrimaryKeyConstraint('user_uuid'),
    schema='settings'
    )
    op.create_table('subscription',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_uuid', sa.UUID(), nullable=False),
    sa.Column('subscription_id', sa.Integer(), nullable=False),
    sa.Column('date_start', sa.DATE(), nullable=True),
    sa.Column('date_end', sa.DATE(), nullable=False),
    sa.Column('payment', sa.Float(), nullable=False),
    sa.Column('currency_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['subscription_id'], ['subscription.subscription_type.id'], ),
    sa.ForeignKeyConstraint(['user_uuid'], ['user.user.uuid'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='subscription'
    )
    op.create_table('team',
    sa.Column('uuid', sa.UUID(), nullable=False),
    sa.Column('owner_id', sa.UUID(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('image', sa.String(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('member_description', sa.Text(), nullable=True),
    sa.Column('privacy', sa.JSON(), nullable=True),
    sa.Column('created_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('deleted_at', sa.TIMESTAMP(), nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['user.user.uuid'], ),
    sa.PrimaryKeyConstraint('uuid'),
    sa.UniqueConstraint('uuid'),
    schema='team'
    )
    op.create_table('cv',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_uuid', sa.UUID(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['user_uuid'], ['user.user.uuid'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='user'
    )
    op.create_table('notification',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_uuid', sa.UUID(), nullable=False),
    sa.Column('image', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['user_uuid'], ['user.user.uuid'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='user'
    )
    op.create_table('message_file',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('message_id', sa.Integer(), nullable=False),
    sa.Column('file_url', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['message_id'], ['chat.message.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='chat'
    )
    op.create_table('message_image',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('message_id', sa.Integer(), nullable=False),
    sa.Column('image_url', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['message_id'], ['chat.message.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='chat'
    )
    op.create_table('cv_response',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('team_uuid', sa.UUID(), nullable=False),
    sa.Column('cv_id', sa.Integer(), nullable=False),
    sa.Column('status_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['cv_id'], ['user.cv.id'], ),
    sa.ForeignKeyConstraint(['status_id'], ['response.response_status.id'], ),
    sa.ForeignKeyConstraint(['team_uuid'], ['team.team.uuid'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='response'
    )
    op.create_table('message_response',
    sa.Column('message_id', sa.Integer(), nullable=False),
    sa.Column('response_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['message_id'], ['chat.message.id'], ),
    sa.ForeignKeyConstraint(['response_id'], ['response.ad_response.id'], ),
    sa.PrimaryKeyConstraint('message_id', 'response_id'),
    schema='response'
    )
    op.create_table('cv_skill',
    sa.Column('cv_id', sa.Integer(), nullable=False),
    sa.Column('skill_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['cv_id'], ['user.cv.id'], ),
    sa.ForeignKeyConstraint(['skill_id'], ['skill.skill.id'], ),
    sa.PrimaryKeyConstraint('cv_id', 'skill_id'),
    schema='skill'
    )
    op.create_table('ad',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('team_uuid', sa.UUID(), nullable=False),
    sa.Column('speciality', sa.String(), nullable=True),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('is_hide', sa.Boolean(), nullable=False),
    sa.Column('is_promoting', sa.Boolean(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('deleted_at', sa.TIMESTAMP(), nullable=True),
    sa.ForeignKeyConstraint(['team_uuid'], ['team.team.uuid'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='team'
    )
    op.create_table('team_experience',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('team_uuid', sa.UUID(), nullable=False),
    sa.Column('date_from', sa.TIMESTAMP(), nullable=True),
    sa.Column('date_to', sa.TIMESTAMP(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['team_uuid'], ['team.team.uuid'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='team'
    )
    op.create_table('team_role',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('team_uuid', sa.UUID(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['team_uuid'], ['team.team.uuid'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='team'
    )
    op.create_table('user_team',
    sa.Column('user_uuid', sa.UUID(), nullable=False),
    sa.Column('team_uuid', sa.UUID(), nullable=False),
    sa.Column('speciality', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['team_uuid'], ['team.team.uuid'], ),
    sa.ForeignKeyConstraint(['user_uuid'], ['user.user.uuid'], ),
    sa.PrimaryKeyConstraint('user_uuid', 'team_uuid'),
    schema='team'
    )
    op.create_table('cv_contact',
    sa.Column('cv_id', sa.Integer(), nullable=False),
    sa.Column('contact_id', sa.Integer(), nullable=False),
    sa.Column('contact_data', sa.String(), nullable=True),
    sa.Column('is_preferred', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['contact_id'], ['user.contact_type.id'], ),
    sa.ForeignKeyConstraint(['cv_id'], ['user.cv.id'], ),
    sa.PrimaryKeyConstraint('cv_id', 'contact_id'),
    schema='user'
    )
    op.create_table('education',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('cv_id', sa.Integer(), nullable=False),
    sa.Column('date_from', sa.TIMESTAMP(), nullable=True),
    sa.Column('date_to', sa.TIMESTAMP(), nullable=True),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['cv_id'], ['user.cv.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='user'
    )
    op.create_table('user_experience',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('cv_id', sa.Integer(), nullable=False),
    sa.Column('date_from', sa.TIMESTAMP(), nullable=True),
    sa.Column('date_to', sa.TIMESTAMP(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['cv_id'], ['user.cv.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='user'
    )
    op.create_table('ad_skill',
    sa.Column('ad_id', sa.Integer(), nullable=False),
    sa.Column('skill_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['ad_id'], ['team.ad.id'], ),
    sa.ForeignKeyConstraint(['skill_id'], ['skill.skill.id'], ),
    sa.PrimaryKeyConstraint('ad_id', 'skill_id'),
    schema='team'
    )
    op.create_table('team_role_permission',
    sa.Column('role_id', sa.Integer(), nullable=False),
    sa.Column('permission_id', sa.Integer(), nullable=False),
    sa.Column('value', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['permission_id'], ['team.team_permission.id'], ),
    sa.ForeignKeyConstraint(['role_id'], ['team.team_role.id'], ),
    sa.PrimaryKeyConstraint('role_id', 'permission_id'),
    schema='team'
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('team_role_permission', schema='team')
    op.drop_table('ad_skill', schema='team')
    op.drop_table('user_experience', schema='user')
    op.drop_table('education', schema='user')
    op.drop_table('cv_contact', schema='user')
    op.drop_table('user_team', schema='team')
    op.drop_table('team_role', schema='team')
    op.drop_table('team_experience', schema='team')
    op.drop_table('ad', schema='team')
    op.drop_table('cv_skill', schema='skill')
    op.drop_table('message_response', schema='response')
    op.drop_table('cv_response', schema='response')
    op.drop_table('message_image', schema='chat')
    op.drop_table('message_file', schema='chat')
    op.drop_table('notification', schema='user')
    op.drop_table('cv', schema='user')
    op.drop_table('team', schema='team')
    op.drop_table('subscription', schema='subscription')
    op.drop_table('settings', schema='settings')
    op.drop_table('message', schema='chat')
    op.drop_table('user', schema='user')
    op.drop_table('sale', schema='subscription')
    op.drop_table('chat_member', schema='chat')
    op.drop_table('role', schema='user')
    op.drop_table('contact_type', schema='user')
    op.drop_table('team_permission', schema='team')
    op.drop_table('subscription_type', schema='subscription')
    op.drop_table('currency', schema='subscription')
    op.drop_table('speciality', schema='skill')
    op.drop_table('skill', schema='skill')
    op.drop_table('user_privacy', schema='settings')
    op.drop_table('privacy', schema='settings')
    op.drop_table('response_status', schema='response')
    op.drop_table('ad_response', schema='response')
    op.drop_table('chat', schema='chat')
    # ### end Alembic commands ###
