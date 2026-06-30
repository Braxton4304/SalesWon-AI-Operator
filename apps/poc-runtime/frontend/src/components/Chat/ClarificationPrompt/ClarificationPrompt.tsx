import "./ClarificationPrompt.css";

interface Props {
  content: string;
}

export function ClarificationPrompt({ content }: Props) {
  return (
    <div className="clarification-prompt">
      <strong>Clarification needed</strong>
      <p>{content}</p>
    </div>
  );
}
