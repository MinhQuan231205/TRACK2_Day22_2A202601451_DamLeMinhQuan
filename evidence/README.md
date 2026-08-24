# Evidence — Day 22: LangSmith + Prompt Versioning

## Kết quả RAGAS: V1 vs V2

| Metric | V1 (ngắn gọn) | V2 (có cấu trúc) | Thắng |
|---|---|---|---|
| faithfulness | **0.9597** | 0.7718 | V1 |
| answer_relevancy | 0.8913 | 0.8933 | V2 (chênh không đáng kể) |
| context_recall | 0.9800 | 0.9800 | Hòa |
| context_precision | 0.9183 | 0.9117 | V1 |

Nguồn: [`03_ragas_report.json`](03_ragas_report.json) — chạy đầy đủ 50 QA pairs × 2 phiên bản
prompt × 4 chỉ số RAGAS (LLM: DeepSeek `deepseek-chat`, embeddings: Ollama `nomic-embed-text`).

## Phân tích: vì sao V1 có faithfulness cao hơn hẳn V2

- **V1** yêu cầu câu trả lời ngắn gọn (2-4 câu), đi thẳng vào trọng tâm, và nói thẳng "không biết"
  nếu context không có thông tin. Câu trả lời ngắn khiến mô hình ít có cơ hội thêm chi tiết không
  được context hỗ trợ trực tiếp.
- **V2** yêu cầu câu trả lời dài hơn, có cấu trúc 3 phần (tóm tắt → trích dẫn nguồn → mức độ chắc
  chắn). Cấu trúc "3-5 câu" này đẩy mô hình phải diễn giải/mở rộng thêm để lấp đầy các phần, và
  phần "nêu mức độ chắc chắn" đặc biệt dễ sinh ra các nhận định suy diễn không bám sát 1:1 vào
  context gốc — đây chính là nguyên nhân kéo faithfulness của V2 xuống thấp hơn đáng kể.
- Ngược lại, `answer_relevancy` và `context_recall` gần như ngang nhau giữa 2 phiên bản vì cả hai
  đều dùng chung retriever (k=3) và đều trả lời đúng trọng tâm câu hỏi — sự khác biệt chỉ nằm ở
  việc V2 "nói nhiều hơn" chứ không lạc đề.

**Kết luận:** với knowledge-base cố định và yêu cầu độ trung thực cao, prompt ngắn gọn, có ràng
buộc "không biết thì nói không biết" (V1) đáng tin cậy hơn cho các ứng dụng cần độ chính xác RAG
cao. V2 phù hợp hơn khi người dùng cần câu trả lời có giải thích/ngữ cảnh phong phú và chấp nhận
đánh đổi một phần độ trung thực.
