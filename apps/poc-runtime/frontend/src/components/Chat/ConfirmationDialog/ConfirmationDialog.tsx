import "./ConfirmationDialog.css";

interface Props {
  proposedAction?: Record<string, unknown> | null;
  pendingId?: string | null;
  onConfirm: (pendingId: string) => void;
  loading?: boolean;
}

export function ConfirmationDialog({
  proposedAction,
  pendingId,
  onConfirm,
  loading,
}: Props) {
  if (!pendingId || !proposedAction) return null;

  return (
    <div className="confirmation-dialog">
      <strong>Confirm update</strong>
      <pre>{JSON.stringify(proposedAction, null, 2)}</pre>
      <button
        type="button"
        disabled={loading}
        onClick={() => onConfirm(pendingId)}
      >
        Confirm update
      </button>
    </div>
  );
}
