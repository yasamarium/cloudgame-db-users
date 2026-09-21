import json
import time

def sync_user_profile(user_id, updates):
    with open('data/users.json', 'r') as f:
        users = json.load(f)
    found = False
    for u in users:
        if u['user_id'] == user_id:
            u.update(updates)
            u['last_login'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
            found = True
            break
    if not found:
        new_user = {
            'user_id': user_id,
            'username': updates.get('username', 'Player'),
            'created_at': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
            'last_login': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
            'playtime_minutes': 0,
            'favorite_games': [],
            'game_saves': {},
            'settings': {'stream_quality': 'high', 'control_mode': 'keyboard_mouse'}
        }
        users.append(new_user)
    with open('data/users.json', 'w') as f:
        json.dump(users, f, indent=2)
    print(f'Synced user {user_id}')
