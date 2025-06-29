from flask import Flask, request, jsonify
from flask_cors import CORS
import re
import nltk
from collections import Counter

app = Flask(__name__)
CORS(app)

# Baixar recursos do NLTK na inicialização
try:
    nltk.download('punkt', quiet=True)
    nltk.download('stopwords', quiet=True)
except:
    pass

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy", "service": "trained-model"})

@app.route('/analyze-competencies', methods=['POST'])
def analyze_competencies():
    try:
        data = request.get_json()
        text = data.get('text', '')
        
        if not text:
            return jsonify({"error": "Texto não fornecido"}), 400
        
        # Análise básica das competências do ENEM
        analysis = {
            "competencia_1": analyze_formal_language(text),
            "competencia_2": analyze_theme_understanding(text),
            "competencia_3": analyze_argumentation(text),
            "competencia_4": analyze_cohesion(text),
            "competencia_5": analyze_proposal(text),
            "overall_score": 0,
            "feedback": [],
            "service": "trained-model"
        }
        
        # Calcular pontuação geral
        scores = [analysis[f"competencia_{i}"]["score"] for i in range(1, 6)]
        analysis["overall_score"] = sum(scores) / len(scores)
        
        return jsonify(analysis)
    
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e),
            "service": "trained-model"
        }), 500

def analyze_formal_language(text):
    """Competência 1: Domínio da modalidade escrita formal da língua portuguesa"""
    errors = []
    score = 200  # Pontuação máxima
    
    # Verificações básicas
    if len(text) < 100:
        errors.append("Texto muito curto")
        score -= 50
    
    # Verificar uso de gírias ou linguagem informal
    informal_words = ['né', 'pra', 'tá', 'vc', 'q', 'tbm']
    for word in informal_words:
        if word in text.lower():
            errors.append(f"Linguagem informal detectada: '{word}'")
            score -= 20
    
    return {
        "score": max(0, score),
        "errors": errors,
        "description": "Domínio da modalidade escrita formal da língua portuguesa"
    }

def analyze_theme_understanding(text):
    """Competência 2: Compreender a proposta de redação e aplicar conceitos das várias áreas de conhecimento"""
    score = 200
    feedback = []
    
    # Verificar se o texto tem desenvolvimento temático
    paragraphs = text.split('\n\n')
    if len(paragraphs) < 3:
        feedback.append("Texto precisa de mais desenvolvimento em parágrafos")
        score -= 50
    
    return {
        "score": max(0, score),
        "feedback": feedback,
        "description": "Compreender a proposta de redação e aplicar conceitos"
    }

def analyze_argumentation(text):
    """Competência 3: Selecionar, relacionar, organizar e interpretar informações, fatos, opiniões e argumentos"""
    score = 200
    feedback = []
    
    # Verificar presença de conectivos argumentativos
    connectives = ['portanto', 'assim', 'logo', 'consequentemente', 'por isso', 'dessa forma']
    found_connectives = [conn for conn in connectives if conn in text.lower()]
    
    if len(found_connectives) < 2:
        feedback.append("Poucos conectivos argumentativos encontrados")
        score -= 30
    
    return {
        "score": max(0, score),
        "feedback": feedback,
        "description": "Selecionar, relacionar, organizar e interpretar informações"
    }

def analyze_cohesion(text):
    """Competência 4: Demonstrar conhecimento dos mecanismos linguísticos necessários para a construção da argumentação"""
    score = 200
    feedback = []
    
    # Verificar repetição excessiva de palavras
    words = re.findall(r'\b\w+\b', text.lower())
    word_count = Counter(words)
    repeated_words = [word for word, count in word_count.items() if count > 5 and len(word) > 3]
    
    if repeated_words:
        feedback.append(f"Palavras repetidas excessivamente: {', '.join(repeated_words[:3])}")
        score -= 20
    
    return {
        "score": max(0, score),
        "feedback": feedback,
        "description": "Demonstrar conhecimento dos mecanismos linguísticos"
    }

def analyze_proposal(text):
    """Competência 5: Elaborar proposta de intervenção para o problema abordado"""
    score = 200
    feedback = []
    
    # Verificar presença de proposta de solução
    proposal_indicators = ['proposta', 'solução', 'medida', 'ação', 'implementar', 'governo', 'sociedade']
    found_indicators = [ind for ind in proposal_indicators if ind in text.lower()]
    
    if len(found_indicators) < 3:
        feedback.append("Proposta de intervenção pouco desenvolvida")
        score -= 50
    
    return {
        "score": max(0, score),
        "feedback": feedback,
        "description": "Elaborar proposta de intervenção para o problema abordado"
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)

