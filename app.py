from flask import Flask, request, jsonify

app = Flask(__name__)

print('hello jsp')

# Liste temporaire pour stocker les tâches
tasks = [
    {
        "id": 1,
        "title": "Réunion matinale",
        "description": "Réunion d'équipe pour discuter des priorités de la journée"
    },
    {
        "id": 2,
        "title": "Développement de fonctionnalité A",
        "description": "Travail sur la mise en œuvre de la fonctionnalité A du projet"
    },
    {
        "id": 3,
        "title": "Pause déjeuner",
        "description": "Temps pour se détendre et recharger ses batteries"
    },
    {
        "id": 4,
        "title": "Répondre aux e-mails",
        "description": "Consacrer du temps à répondre aux e-mails et aux messages"
    },
    {
        "id": 5,
        "title": "Réunion client",
        "description": "Discussion avec le client pour discuter des exigences et des retours"
    },
    {
        "id": 6,
        "title": "Tests unitaires",
        "description": "Écriture et exécution de tests unitaires pour assurer la qualité du code"
    },
    {
        "id": 7,
        "title": "Développement de fonctionnalité B",
        "description": "Travail sur la mise en œuvre de la fonctionnalité B du projet"
    },
    {
        "id": 8,
        "title": "Formation interne",
        "description": "Participation à une formation interne pour acquérir de nouvelles compétences"
    },
    {
        "id": 9,
        "title": "Révision de code",
        "description": "Examen du code avec les collègues pour garantir la qualité du code"
    },
    {
        "id": 10,
        "title": "Pause café",
        "description": "Courte pause pour prendre un café et socialiser avec les collègues"
    },
    {
        "id": 11,
        "title": "Planification de projet",
        "description": "Réunion pour discuter de la planification du projet à venir"
    },
    {
        "id": 12,
        "title": "Support client",
        "description": "Répondre aux demandes de support client et résoudre les problèmes signalés"
    },
    {
        "id": 13,
        "title": "Développement de fonctionnalité C",
        "description": "Travail sur la mise en œuvre de la fonctionnalité C du projet"
    },
    {
        "id": 14,
        "title": "Pause déjeuner",
        "description": "Temps pour se détendre et recharger ses batteries"
    },
    {
        "id": 15,
        "title": "Réunion d'équipe",
        "description": "Réunion d'équipe pour discuter des progrès et des obstacles"
    },
    {
        "id": 16,
        "title": "Tests d'intégration",
        "description": "Exécution de tests d'intégration pour garantir le bon fonctionnement global du système"
    },
    {
        "id": 17,
        "title": "Développement de fonctionnalité D",
        "description": "Travail sur la mise en œuvre de la fonctionnalité D du projet"
    },
    {
        "id": 18,
        "title": "Réunion de revue de code",
        "description": "Réunion pour discuter des résultats de la revue de code"
    },
    {
        "id": 19,
        "title": "Documentation",
        "description": "Élaboration de la documentation du projet pour les utilisateurs finaux"
    },
    {
        "id": 20,
        "title": "Fin de la journée",
        "description": "Clôture des tâches en cours et planification des travaux du lendemain"
    }
]


# Routes CRUD
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task:
        return jsonify(task)
    else:
        return jsonify({'message': 'Task not found'}), 404

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    new_task = {
        'id': len(tasks) + 1,
        'title': data['title'],
        'description': data.get('description', '')
    }
    tasks.append(new_task)
    return jsonify({'message': 'Task created successfully'}), 201

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task:
        data = request.get_json()
        task['title'] = data['title']
        task['description'] = data.get('description', '')
        return jsonify({'message': 'Task updated successfully'})
    else:
        return jsonify({'message': 'Task not found'}), 404

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return jsonify({'message': 'Task deleted successfully'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
