import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'clinic_management.settings')
django.setup()

from django.template import Template, Context

try:
    # Test widget template
    with open('templates/ai_chatbox/widget.html', 'r', encoding='utf-8') as f:
        template_content = f.read()
    
    template = Template(template_content)
    context = Context({})
    rendered = template.render(context)
    
    print("✅ Widget template syntax OK")
    print(f"✅ Template length: {len(rendered)} characters")
    
    # Test chat template
    with open('templates/ai_chatbox/chat.html', 'r', encoding='utf-8') as f:
        template_content = f.read()
    
    template = Template(template_content)
    rendered = template.render(context)
    
    print("✅ Chat template syntax OK")
    print("✅ All templates validated successfully!")
    
except Exception as e:
    print(f"❌ Template error: {e}")
    import traceback
    traceback.print_exc()