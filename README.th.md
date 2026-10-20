# Claude Starter Brain

**สมองสำเร็จรูปให้ Claude Code** clone โฟลเดอร์นี้ไป แล้วเปิด `claude` ข้างใน แค่นั้น AI จะจำได้ว่าคุณเป็นใคร ชอบทำงานแบบไหน และเคยพลาดอะไรมาแล้วบ้าง จำข้าม session ตลอด ความจำทั้งหมดเก็บเป็นไฟล์ Markdown ธรรมดา เปิดอ่านใน Obsidian เองได้

[English](README.md)

ทำมาให้คนที่เพิ่งเริ่มใช้ AI agent ไม่ต้องเขียนโค้ด ตั้งค่าประมาณ 10 นาที

## ได้อะไรบ้าง

- **จำได้จริง** `CLAUDE.md` สั่งให้ Claude อ่าน `Brain/00_Index.md` ทุกครั้งที่เริ่มแชท แล้วเขียนเรื่องที่ควรจำกลับลง vault แบบเรื่องละไฟล์ ลิงก์กันด้วย `[[ ]]` และลงสารบัญทุกครั้ง
- **พลาดแล้วจำ** เจอ error เมื่อไหร่ Claude จะจดว่าเกิดอะไร ต้นเหตุคืออะไร แก้ยังไง ลง `Brain/lessons/` รอบหน้าจะอ่านก่อนเลยไม่พลาดซ้ำ
- **`/onboard`** ถามสั้นๆ ประมาณ 9 ข้อ (เรียกกันว่าอะไร โทนการพูด ภาษา ความยาวคำตอบ ทำงานอะไร ข้อห้าม) แล้วบันทึกลง vault ให้เอง
- **ใช้กับ Obsidian ได้** เปิด `Brain/` เป็น vault แล้ว Graph View จะโชว์ว่าความรู้ของ AI เชื่อมกันยังไง และโตขึ้นเรื่อยๆ
- **มี skill ให้ 4 ตัว**
  - `/onboard` ตั้งค่าครั้งแรก
  - `youtube` วางลิงก์คลิปแล้วได้ transcript + สรุป จะเซฟลง vault ด้วยก็ได้
  - `notebooklm` ใช้ Google NotebookLM ทำโน้ตบุ๊กหรือ podcast
  - `manual` Claude อ่าน skill ของตัวเองแล้วสร้าง `manual.html` คู่มือเลยไม่เคยเก่า
- **ค่าเริ่มต้นปลอดภัย** งานใหญ่บอกแผนก่อน จะลบหรือเขียนทับไฟล์ต้องถามก่อน ไม่ commit secret ทำแค่ที่สั่ง

## ติดตั้ง

1. ติดตั้ง [Claude Code](https://docs.claude.com/en/docs/claude-code): `npm install -g @anthropic-ai/claude-code`
2. โหลดโฟลเดอร์ไปเก็บที่ถาวร (อย่าทิ้งไว้ใน Downloads)
   ```
   git clone https://github.com/chenlab789/claude-starter-brain.git
   cd claude-starter-brain
   ```
   ไม่มี git ก็กด **Code → Download ZIP** แล้วแตกไฟล์
3. เปิด Claude **ในโฟลเดอร์นี้** มันถึงจะอ่าน `CLAUDE.md`
   ```
   claude
   ```
4. พิมพ์ `/onboard` แล้วตอบคำถาม
5. *(ไม่บังคับ)* ลง [Obsidian](https://obsidian.md) เลือก **Open folder as vault** แล้วชี้ไปที่ `Brain/`
6. *(ไม่บังคับ)* ถ้าจะใช้ skill YouTube: `pip install youtube-transcript-api`

## ลองดู

- *"อ่าน index แล้วบอกหน่อยว่าตอนนี้รู้อะไรเกี่ยวกับเราบ้าง"*
- *"ชอบให้ตอบเป็น bullet มากกว่าเป็นย่อหน้า จำไว้ด้วย"* แล้วเปิด `Brain/preferences.md` ดู
- *"ทำอะไรได้บ้าง"* Claude จะสร้าง `manual.html` ใหม่ให้เปิดดู

## ปรับแต่ง

ทุกอย่างเป็น Markdown ธรรมดา อยากเปลี่ยนนิสัย AI ก็แก้ `Brain/identity/ai-persona.md` หรือบอก Claude ตรงๆ ว่า *"ต่อไปพูดแบบนี้นะ"* มันจะแก้ไฟล์ให้เอง จะเพิ่ม skill ก็สร้าง `.claude/skills/<ชื่อ>/SKILL.md` แล้ว skill นั้นจะขึ้นในคู่มือเอง

## License

MIT
