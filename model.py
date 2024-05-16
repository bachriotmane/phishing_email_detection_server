from huggingface_hub import login
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
login(token="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")

def model(text):
    label =[]
    

        # Tokenize the spam email
    print(text)
    model = AutoModelForSequenceClassification.from_pretrained("cybersectony/phishing-email-detection-distilbert")
    tokenizer = AutoTokenizer.from_pretrained("cybersectony/phishing-email-detection-distilbert")
    inputs = tokenizer(text, return_tensors="pt")
    logits = model(**inputs).logits
    probabilities = torch.nn.functional.softmax(logits, dim=-1)
    print(probabilities)
    predicted_class_id = probabilities.argmax().item()
    print(predicted_class_id)
    label_map = {0: "negative", 1: "positive"}
    predicted_label = label_map[predicted_class_id]
    return predicted_label


spam_email = """
        Dear Otmane,

        You have a new message.

        From: Murat, Sales Account Manager Medianova CDN & Cloud Security
        Message: Hi Otmane, Hope you are doing great! I noticed that you'll be attending GITEX AFRICA too, and I wanted to share that Medianova will also be there as an exhibitor. At GITEX. We will be introducing Aksela, our cutting edge product and a compelling alternative to Cloudflare. Aksela offers services such as Web Application Firewall (WAF), Rate Limiting, and robust DDoS mitigation, and it has been undergoing significant growth recently. Feel free to explore Aksela’s page for comphrehensive details, including a product showcase video and customer success stories; https://linktr.ee/medianova_cdn I would love to arrange a quick catch up to discuss how Aksela can secure your web properties. You’ll easily spot us at Hall 2, 2A-10. Feel free to book a meeting at your convenience through this portal. Looking forward to hearing from you soon. Best, Murat

        To reply click the button 
        """
model(spam_email)