

import firebase_admin
from firebase_admin import credentials, firestore
import google.generativeai as genai

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

genai.configure(api_key="AIzaSyBKfKea1v9XuwqP0XZCWRR63vqfw-Zh5sQ")
model = genai.GenerativeModel("gemini-1.5-pro")

def translate_text(text):
    if not text or not isinstance(text, str):
        return text
    prompt = f"""Traduza o texto abaixo para inglês, mantendo o formato original e qualquer markdown ou estrutura de formatação presente. Não altere a estrutura de listas, negrito, itálico ou links. Apenas traduza o conteúdo textual.

Texto original:
{text}
"""
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        print(f"Erro ao traduzir: {e}")
        return text

def delete_collection(coll_name):
    print(f"Limpando coleção: {coll_name}")
    docs = db.collection(coll_name).stream()
    deleted = 0
    for doc in docs:
        doc.reference.delete()
        deleted += 1
        print(f" - Deletado: {doc.id}")
    print(f"Total deletado: {deleted}")

def clone_and_translate(source, target):
    print(f"Lendo documentos da coleção: {source}")
    docs = db.collection(source).stream()
    created = 0
    skipped = 0
    for doc in docs:
        data = doc.to_dict()
        if not data:
            print(f"Documento vazio: {doc.id}")
            skipped += 1
            continue
        translated = {}
        for k, v in data.items():
            if isinstance(v, str):
                translated[k] = translate_text(v)
            elif isinstance(v, list):
                translated[k] = [translate_text(i) if isinstance(i, str) else i for i in v]
            else:
                translated[k] = v
        db.collection(target).document(doc.id).set(translated)
        print(f"Documento traduzido e salvo: {doc.id}")
        created += 1
    return created, skipped

if __name__ == "__main__":
    import os
    import sys
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    print("Iniciando migração e tradução")
    delete_collection("projects-ing")
    created, skipped = clone_and_translate("projects", "projects-ing")
    print(f"Finalizado. Documentos criados: {created}, pulados: {skipped}")
